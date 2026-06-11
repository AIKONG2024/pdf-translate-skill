from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path

from validate_outputs import ValidationError, validate_outputs

CLOUD_SERVICES = frozenset(
    {
        "google",
        "bing",
        "deepl",
        "deeplx",
        "openai",
        "azure-openai",
        "gemini",
        "azure",
        "tencent",
        "dify",
        "anythingllm",
        "grok",
        "deepseek",
        "minimax",
        "openailiked",
        "zhipu",
        "modelscope",
        "silicon",
    },
)


class TranslateError(Exception):
    pass


@dataclass(frozen=True, slots=True)
class RunResult:
    run_dir: str
    source_copy: str
    final_pdf: str
    summary: str
    engine: str
    service: str
    source_language: str
    target_language: str


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_pdf", type=Path)
    parser.add_argument("--engine", default="pdf2zh", choices=("pdf2zh", "mock"))
    parser.add_argument("--source", default="auto")
    parser.add_argument("--target", required=True)
    parser.add_argument("--service", default="google")
    parser.add_argument("--out", default="outputs/pdf_translate", type=Path)
    parser.add_argument("--thread", default="1")
    parser.add_argument("--confirm-cloud", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--keep-renders", action="store_true")
    return parser


def service_key(service: str) -> str:
    return service.split(":", 1)[0].lower()


def require_cloud_confirmation(service: str, confirmed: bool) -> None:
    if service_key(service) in CLOUD_SERVICES and not confirmed:
        raise TranslateError(f"service '{service}' requires --confirm-cloud")


def make_run_dir(output_root: Path, input_pdf: Path) -> Path:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    stem = "".join(ch if ch.isalnum() or ch in ("-", "_") else "-" for ch in input_pdf.stem)
    run_dir = output_root / f"{stamp}-{stem[:48]}"
    run_dir.mkdir(parents=True, exist_ok=False)
    (run_dir / "source").mkdir()
    return run_dir


def copy_source(input_pdf: Path, run_dir: Path) -> Path:
    if not input_pdf.exists():
        raise TranslateError(f"input PDF is missing: {input_pdf}")
    if input_pdf.suffix.lower() != ".pdf":
        raise TranslateError(f"input file must be a PDF: {input_pdf}")
    source_copy = run_dir / "source" / input_pdf.name
    shutil.copy2(input_pdf, source_copy)
    return source_copy


def run_mock_engine(source_copy: Path, run_dir: Path) -> None:
    shutil.copy2(source_copy, run_dir / f"{source_copy.stem}-mono.pdf")


def pdf2zh_binary() -> str:
    configured = os.environ.get("PDF2ZH_BIN")
    if configured:
        return configured
    found = shutil.which("pdf2zh")
    if found:
        return found
    raise TranslateError("pdf2zh executable not found; install official PDFMathTranslate pdf2zh")


def run_pdf2zh_engine(args: argparse.Namespace, source_copy: Path, run_dir: Path) -> None:
    if args.source == "auto":
        raise TranslateError("source language must be confirmed before running pdf2zh")
    command = [
        pdf2zh_binary(),
        str(source_copy),
        "--lang-in",
        args.source,
        "--lang-out",
        args.target,
        "--service",
        args.service,
        "--thread",
        args.thread,
        "--output",
        str(run_dir),
    ]
    completed = subprocess.run(command, text=True, capture_output=True, check=False)
    if completed.returncode != 0:
        raise TranslateError(completed.stderr.strip() or completed.stdout.strip())


def normalize_output(run_dir: Path, target: str) -> Path:
    final_pdf = run_dir / f"translated-{target}.pdf"
    mono_candidates = sorted(run_dir.glob("*-mono.pdf"))
    if not mono_candidates:
        raise TranslateError("engine did not produce a *-mono.pdf file")
    shutil.copy2(mono_candidates[0], final_pdf)
    for dual_pdf in run_dir.glob("*-dual.pdf"):
        dual_pdf.unlink()
    return final_pdf


def write_summary(result: RunResult) -> None:
    path = Path(result.summary)
    lines = [
        "# Translation Summary",
        "",
        f"- engine: {result.engine}",
        f"- service: {result.service}",
        f"- source_language: {result.source_language}",
        f"- target_language: {result.target_language}",
        f"- final_pdf: {result.final_pdf}",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def execute(args: argparse.Namespace) -> RunResult:
    require_cloud_confirmation(args.service, args.confirm_cloud)
    if args.dry_run:
        raise TranslateError("dry run passed validation; remove --dry-run to execute")
    run_dir = make_run_dir(args.out, args.input_pdf)
    source_copy = copy_source(args.input_pdf, run_dir)
    if args.engine == "mock":
        run_mock_engine(source_copy, run_dir)
    if args.engine == "pdf2zh":
        run_pdf2zh_engine(args, source_copy, run_dir)
    final_pdf = normalize_output(run_dir, args.target)
    summary = run_dir / "translation-summary.md"
    result = RunResult(
        run_dir=str(run_dir),
        source_copy=str(source_copy),
        final_pdf=str(final_pdf),
        summary=str(summary),
        engine=args.engine,
        service=args.service,
        source_language=args.source,
        target_language=args.target,
    )
    write_summary(result)
    validate_outputs(source_copy, final_pdf, run_dir, args.keep_renders)
    return result


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        result = execute(args)
    except (TranslateError, ValidationError) as exc:
        print(str(exc), file=sys.stderr)
        return 2 if "requires --confirm-cloud" in str(exc) else 1
    print(json.dumps(asdict(result), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
