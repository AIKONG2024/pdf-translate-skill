# pdf-translate-skill

[KOREAN](README.ko.md)

Agent skill for translating PDFs while preserving layout as much as the selected engine allows.

- Works with Codex, Claude Code, and agents-compatible runtimes
- Uses the official `pdf2zh` CLI from PDFMathTranslate as the default engine
- Produces a final translated PDF

-그림위치-

## Install

### Human

Ask your agent:

```text
AIKONG2024/pdf-translate-skill 스킬 설정해줘
```

### Agent

<details>
<summary>Open install instructions</summary>

Read this repository and install the `pdf-translate` skill into the skill directory used by the current agent runtime.

The skill folder to install is:

```text
pdf-translate/
```

The installed skill must include:

```text
pdf-translate/SKILL.md
pdf-translate/scripts/
pdf-translate/references/
pdf-translate/agents/
```

Use the installation method supported by the current runtime:

- If the runtime supports GitHub skill installation, install `AIKONG2024/pdf-translate-skill` with path `pdf-translate`.
- If the runtime supports the `skills` CLI, use:

```bash
npx --yes skills add https://github.com/AIKONG2024/pdf-translate-skill --all -g
```

- If the runtime only supports manual local skills, copy the `pdf-translate/` folder into that runtime's skill directory.

After installing the skill, check the runtime dependency:

```bash
pdf2zh --help
```

If `pdf2zh` is missing, install the official PDFMathTranslate CLI:

```bash
python -m pip install pdf2zh
```

If the runtime requires restart or reload to discover new skills, tell the user to restart or reload it.

</details>

## Setup

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
