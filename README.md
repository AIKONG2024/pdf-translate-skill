# pdf-translate-skill

Translate PDFs through an agent while preserving layout as much as the selected engine allows.

- Codex, Claude Code, and agents-compatible runtimes
- Default engine: official `pdf2zh` CLI from PDFMathTranslate
- Output: final translated PDF

-그림위치-

## What It Does

| Task | Skill | Description | User key required | Docs |
| --- | --- | --- | --- | --- |
| PDF translation | `pdf-translate` | Translate text-based PDFs, preserve layout, normalize output, and run basic QA | Optional | [Guide](docs/features/pdf-translate.md) |

## Dependency Disclosure

This skill uses the official `pdf2zh` CLI from PDFMathTranslate as the default PDF layout translation engine.

The skill orchestrates language confirmation, provider setup, privacy confirmation, output normalization, and QA. It does not vendor PDFMathTranslate, BabelDOC, models, wheels, or sample PDFs.

Current official `pdf2zh` releases may install upstream runtime dependencies such as BabelDOC. The skill does not invoke the optional `--babeldoc` backend by default.

## Ask Your Agent To Install

Paste this into Codex or Claude Code:

```text
Read this repository's install guide and install the pdf-translate skill globally. After installation, verify the skill files and tell me the next command to translate a PDF.
```

## Direct Install

```bash
npx --yes skills add https://github.com/<owner>/pdf-translate-skill --all -g
```

For local testing from this repository:

```bash
npx --yes skills add . --all -g
```

Then ask:

```text
Translate this PDF to French while preserving layout: /path/to/paper.pdf
```

## More

- [Install](docs/install.md)
- [Setup](docs/setup.md)
- [Security and secrets](docs/security-and-secrets.md)
- [PDF translate guide](docs/features/pdf-translate.md)
