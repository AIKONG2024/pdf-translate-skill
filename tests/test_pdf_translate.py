from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "pdf-translate" / "scripts" / "pdf_translate.py"
VALIDATE = ROOT / "pdf-translate" / "scripts" / "validate_outputs.py"


def _write_minimal_pdf(path: Path) -> None:
    path.write_bytes(
        b"%PDF-1.4\n"
        b"1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj\n"
        b"2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj\n"
        b"3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 200 200] >> endobj\n"
        b"trailer << /Root 1 0 R >>\n%%EOF\n"
    )


def test_dry_run_reports_cloud_confirmation_requirement(tmp_path: Path) -> None:
    source = tmp_path / "sample.pdf"
    _write_minimal_pdf(source)

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            str(source),
            "--target",
            "fr",
            "--dry-run",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 2
    assert "requires --confirm-cloud" in result.stderr


def test_mock_engine_creates_normalized_translated_pdf(tmp_path: Path) -> None:
    source = tmp_path / "sample.pdf"
    out_dir = tmp_path / "out"
    _write_minimal_pdf(source)

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            str(source),
            "--engine",
            "mock",
            "--source",
            "en",
            "--target",
            "fr",
            "--service",
            "mock-local",
            "--out",
            str(out_dir),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    final_pdf = Path(payload["final_pdf"])
    summary = Path(payload["summary"])
    source_copy = Path(payload["source_copy"])
    assert final_pdf.name == "translated-fr.pdf"
    assert final_pdf.exists()
    assert summary.exists()
    assert source_copy.exists()
    assert not list(Path(payload["run_dir"]).glob("*.png"))


def test_validate_outputs_rejects_missing_final_pdf(tmp_path: Path) -> None:
    source = tmp_path / "source.pdf"
    run_dir = tmp_path / "run"
    run_dir.mkdir()
    _write_minimal_pdf(source)

    result = subprocess.run(
        [
            sys.executable,
            str(VALIDATE),
            "--source",
            str(source),
            "--final",
            str(run_dir / "translated-fr.pdf"),
            "--run-dir",
            str(run_dir),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 1
    assert "final PDF is missing" in result.stderr
