# pdf-translate-skill

Agent skill for translating PDFs while preserving layout as much as the selected engine allows.

- Works with Codex, Claude Code, and agents-compatible runtimes
- Uses the official `pdf2zh` CLI from PDFMathTranslate as the default engine
- Produces a final translated PDF

-그림위치-

## Install

```bash
npx --yes skills add https://github.com/AIKONG2024/pdf-translate-skill --all -g
```

For local development from this repository:

```bash
npx --yes skills add . --all -g
```

## Setup

Install the PDF translation engine:

```bash
python -m pip install pdf2zh
pdf2zh --help
```

If you use a paid or keyed provider, set only the environment variables for that provider.

Common examples:

| Provider | Environment variables |
| --- | --- |
| Google | None |
| DeepL | `DEEPL_AUTH_KEY` |
| OpenAI | `OPENAI_API_KEY`, optional `OPENAI_MODEL` |
| Gemini | `GEMINI_API_KEY`, optional `GEMINI_MODEL` |
| Ollama | `OLLAMA_HOST`, `OLLAMA_MODEL` |

## Use

Ask your agent:

```text
Translate this PDF to French while preserving layout: /path/to/paper.pdf
```

The agent should confirm the source and target language. Before using a cloud translation provider, it must ask whether you approve sending extracted PDF text to that provider.

## Output

```text
outputs/pdf_translate/<run-id>/
├── source/
│   └── original.pdf
├── translated-<target-lang>.pdf
└── translation-summary.md
```

The final file to use is:

```text
translated-<target-lang>.pdf
```

## Notes

- This skill does not vendor PDFMathTranslate, BabelDOC, models, wheels, or sample PDFs.
- Current official `pdf2zh` releases may install upstream runtime dependencies such as BabelDOC.
- This skill does not invoke the optional `--babeldoc` backend by default.
- For scanned/image-only PDFs, run OCR first or expect limited results.
- Detailed usage is in [docs/features/pdf-translate.md](docs/features/pdf-translate.md).
