# do-you-want-translate-pdf-file-skill

[KOREAN](README.ko.md)

Agent skill for translating PDFs while preserving layout as much as the selected engine allows.

- Works with Codex, Claude Code, and agents-compatible runtimes
- Uses the official `pdf2zh` CLI from PDFMathTranslate as the default engine
- Produces a final translated PDF

<img width="450" height="600" alt="image" src="https://github.com/user-attachments/assets/c1cd0770-ae2a-4df3-8f76-679c9da0858b" /><img width="450" height="600" alt="image" src="https://github.com/user-attachments/assets/2f6f2b6e-4e0a-4096-ba81-1334f13d678a" />

## Install

### Human

Ask your agent:

```text
Set up the AIKONG2024/do-you-want-translate-pdf-file-skill skill.
```

### Agent

<details>
<summary>Open install instructions</summary>

Read this repository and install the `do-you-want-translate-pdf-file-skill` skill into the skill directory used by the current agent runtime.

The skill folder to install is:

```text
do-you-want-translate-pdf-file-skill/
```

The installed skill must include:

```text
do-you-want-translate-pdf-file-skill/SKILL.md
do-you-want-translate-pdf-file-skill/scripts/
do-you-want-translate-pdf-file-skill/references/
do-you-want-translate-pdf-file-skill/agents/
```

Use the installation method supported by the current runtime:

- If the runtime supports GitHub skill installation, install `AIKONG2024/do-you-want-translate-pdf-file-skill` with path `do-you-want-translate-pdf-file-skill`.
- If the runtime supports the `skills` CLI, use:

```bash
npx --yes skills add https://github.com/AIKONG2024/do-you-want-translate-pdf-file-skill --all -g
```

- If the runtime only supports manual local skills, copy the `do-you-want-translate-pdf-file-skill/` folder into that runtime's skill directory.

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

Default provider is Google, so no API key is required for a basic run. Cloud providers can receive extracted PDF text, so your agent must ask for confirmation before running them.

For higher quality or local/private translation, choose a provider and set only that provider's environment variables.

| Provider | Service | Environment variables |
| --- | --- | --- |
| Google | `google` | None |
| Bing | `bing` | None |
| DeepL | `deepl` | `DEEPL_AUTH_KEY` |
| DeepLX | `deeplx` | `DEEPLX_ENDPOINT` |
| Ollama | `ollama` | `OLLAMA_HOST`, `OLLAMA_MODEL` |
| OpenAI | `openai` | `OPENAI_API_KEY`, optional `OPENAI_BASE_URL`, `OPENAI_MODEL`, `OPENAI_STOP_TOKENS`, `OPENAI_MAX_TOKENS` |
| Azure OpenAI | `azure-openai` | `AZURE_OPENAI_BASE_URL`, `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_MODEL` |
| Gemini | `gemini` | `GEMINI_API_KEY`, optional `GEMINI_MODEL` |
| Azure Translator | `azure` | `AZURE_ENDPOINT`, `AZURE_API_KEY` |
| Tencent | `tencent` | `TENCENTCLOUD_SECRET_ID`, `TENCENTCLOUD_SECRET_KEY` |
| Dify | `dify` | `DIFY_API_URL`, `DIFY_API_KEY` |
| AnythingLLM | `anythingllm` | `AnythingLLM_URL`, `AnythingLLM_APIKEY` |
| Argos Translate | `argos` | Argos language packages |
| Grok | `grok` | `GORK_API_KEY`, `GORK_MODEL` |
| DeepSeek | `deepseek` | `DEEPSEEK_API_KEY`, `DEEPSEEK_MODEL` |
| MiniMax | `minimax` | `MINIMAX_API_KEY`, `MINIMAX_MODEL` |
| OpenAI-compatible | `openailiked` | `OPENAILIKED_BASE_URL`, `OPENAILIKED_API_KEY`, `OPENAILIKED_MODEL`, optional `OPENAILIKED_STOP_TOKENS`, `OPENAILIKED_MAX_TOKENS` |

Examples:

```powershell
# Windows PowerShell
$env:OPENAI_API_KEY="your-api-key"
$env:OPENAI_MODEL="gpt-4o-mini"
```

```bash
# macOS / Linux
export OPENAI_API_KEY="your-api-key"
export OPENAI_MODEL="gpt-4o-mini"
```

For Ollama local translation:

```bash
export OLLAMA_HOST="http://127.0.0.1:11434"
export OLLAMA_MODEL="gemma2"
```

## Use

Ask your agent:

```text
Translate this PDF to Korean while preserving layout.
```

Attach the PDF when you send the request. The agent should confirm the source and target language. Before using a cloud translation provider, it must ask whether you approve sending extracted PDF text to that provider.

## Output

```text
outputs/pdf_translate/<run-id>/
├── source/
│   └── original.pdf
├── translated-<target-lang>.pdf
└── translation-summary.md
```

Final generated file:

```text
translated-<target-lang>.pdf
```

## Attribution And License

This skill uses the official `pdf2zh` CLI from [PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) to translate PDFs while preserving layout.

PDFMathTranslate / `pdf2zh` is distributed under the `AGPL-3.0` license. This repository does not include that library or model files; it is an MIT-licensed skill that guides an agent to run the external `pdf2zh` CLI.
