from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PAGE_PATTERN = re.compile(rb"/Type\s*/Page\b")


class ValidationError(Exception):
    pass


def count_pages(path: Path) -> int:
    data = path.read_bytes()
    return len(PAGE_PATTERN.findall(data))


def require_pdf(path: Path, label: str) -> None:
    if not path.exists():
        raise ValidationError(f"{label} PDF is missing: {path}")
    if not path.is_file():
        raise ValidationError(f"{label} PDF is not a file: {path}")
    if not path.read_bytes().startswith(b"%PDF-"):
        raise ValidationError(f"{label} PDF does not start with %PDF-: {path}")


def validate_outputs(source: Path, final: Path, run_dir: Path, keep_renders: bool) -> None:
    require_pdf(source, "source")
    require_pdf(final, "final")
    source_pages = count_pages(source)
    final_pages = count_pages(final)
    if source_pages > 0 and final_pages > 0 and source_pages != final_pages:
        raise ValidationError(
            f"page count mismatch: source={source_pages}, final={final_pages}",
        )
    if not keep_renders:
        renders = sorted(run_dir.glob("*.png"))
        if renders:
            names = ", ".join(path.name for path in renders)
            raise ValidationError(f"temporary render PNGs remain: {names}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--final", required=True, type=Path)
    parser.add_argument("--run-dir", required=True, type=Path)
    parser.add_argument("--keep-renders", action="store_true")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        validate_outputs(args.source, args.final, args.run_dir, args.keep_renders)
    except ValidationError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print("validation ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
