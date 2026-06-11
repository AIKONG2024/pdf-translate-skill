---
name: pdf-translate
description: Translate text-based PDFs while preserving layout as much as possible using the official pdf2zh CLI from PDFMathTranslate. Use when the user asks to translate a PDF, keep PDF layout, produce a translated PDF, choose a PDF translation provider, or validate PDF translation output.
---

# PDF Translate

## What This Skill Does

Use the official `pdf2zh` CLI from PDFMathTranslate to translate text-based PDFs and return a final translated PDF.

The skill handles language confirmation, provider setup, cloud-transfer confirmation, output normalization, and basic validation.

## When To Use

- "Translate this PDF to English while preserving layout."
- "PDF 논문을 한국어로 번역해서 PDF로 줘."
- "Translate `/path/to/file.pdf` to Japanese."
- "Keep the PDF layout and only provide the translated PDF."

## When Not To Use

- The user needs guaranteed translation of text embedded inside figures.
- The PDF is scanned/image-only and OCR has not been done.
- The user refuses cloud transfer and no local provider is available.
- The user needs a manually typeset publication-grade PDF.

## Prerequisites

- Python 3.11+
- Official `pdf2zh` CLI from PDFMathTranslate
- Provider credentials when the selected service requires them

## Dependency Disclosure

Tell users that the default layout engine is the official `pdf2zh` CLI from PDFMathTranslate.

Do not claim that the skill is independent from PDFMathTranslate. Current official `pdf2zh` releases may install upstream runtime dependencies such as BabelDOC. This skill does not call the optional `--babeldoc` backend by default.

## Required Environment Variables

Read `references/services.md` when a provider needs keys.

Common keyed providers:

- DeepL: `DEEPL_AUTH_KEY`
- OpenAI: `OPENAI_API_KEY`
- Gemini: `GEMINI_API_KEY`
- Azure OpenAI: `AZURE_OPENAI_BASE_URL`, `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_MODEL`
- Ollama: `OLLAMA_HOST`, `OLLAMA_MODEL`

## Workflow

### 1. Confirm Inputs

Confirm:

- PDF path
- source language
- target language
- translation service

If target language is missing, ask for it. If source language is missing, inspect first text-bearing pages, infer the likely source language, and ask the user to confirm the source-to-target pair.

### 2. Confirm Cloud Transfer

Before using Google, Bing, DeepL, OpenAI, Gemini, Azure, Tencent, Dify, AnythingLLM, Grok, DeepSeek, MiniMax, OpenAI-compatible, or similar cloud services, say:

```text
This translation service may send extracted PDF text to an external provider (<provider>). Do you want to continue?
```

Do not proceed with a cloud service until the user confirms.

### 3. Check Runtime

If `pdf2zh` is missing, ask the user to install it:

```bash
python -m pip install pdf2zh
pdf2zh --help
```

If global installation is blocked, use an approved local executable and set `PDF2ZH_BIN`.

### 4. Run Translation

Use the helper:

```bash
python pdf-translate/scripts/pdf_translate.py input.pdf --source en --target fr --service google --confirm-cloud --out outputs/pdf_translate
```

For local package testing only:

```bash
python pdf-translate/scripts/pdf_translate.py input.pdf --engine mock --source en --target fr --service mock-local --out outputs/pdf_translate
```

### 5. Validate Output

The helper runs validation. If validating an existing output:

```bash
python pdf-translate/scripts/validate_outputs.py --source source.pdf --final translated-fr.pdf --run-dir outputs/pdf_translate/run-id
```

## Done When

- The final `translated-<target-lang>.pdf` exists.
- The final PDF opens and starts with a valid PDF header.
- Page count matches when both PDFs expose page markers.
- No temporary render PNGs remain by default.
- The user receives the final translated PDF path.

## Failure Modes

- Missing target language: ask the user.
- Missing source language: infer and ask for confirmation.
- Missing provider key: report the exact environment variable from `references/services.md`.
- Missing cloud confirmation: stop and ask.
- Missing `pdf2zh`: install official PDFMathTranslate `pdf2zh` or set `PDF2ZH_BIN`.
- Scanned/image-only PDF: explain that v1 targets text-based PDFs and may need OCR first.
- Layout corruption: report the limitation and keep the original source copy.

## Notes

- Default service is `google`.
- Default output is translated-only PDF.
- Keep bilingual PDF only when the user explicitly asks for it.
- Do not translate figure-internal labels by default.
