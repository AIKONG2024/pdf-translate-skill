# PDF Translate Guide

## What This Skill Does

`pdf-translate` translates text-based PDFs while preserving layout as much as the selected engine allows.

-그림위치-

## First Requirements

- Python 3.11+
- Official `pdf2zh` CLI from PDFMathTranslate
- Cloud-transfer confirmation before cloud services

## Inputs

- PDF path
- Source language, or permission to infer and confirm it
- Target language
- Translation service

## Basic Flow

1. Confirm the PDF path.
2. Confirm source and target languages.
3. Choose the service. Default is `google`.
4. Ask for cloud-transfer confirmation when needed.
5. Run the helper script.
6. Return the final translated PDF.

## Example Request

```text
Translate this PDF to Japanese while preserving layout: /path/to/paper.pdf
```

## Output

```text
outputs/pdf_translate/<run-id>/
├── source/
│   └── original.pdf
├── translated-<target-lang>.pdf
└── translation-summary.md
```

The user-facing deliverable is `translated-<target-lang>.pdf`.

## Failure Modes

- Missing target language: ask the user.
- Missing source language: infer from sampled text and ask for confirmation.
- Missing cloud confirmation: stop and ask.
- Missing provider key: report the exact environment variable.
- Missing `pdf2zh`: ask the user to install official PDFMathTranslate `pdf2zh`.
- Scanned PDF: explain that v1 is intended for text-based PDFs and may need OCR first.
