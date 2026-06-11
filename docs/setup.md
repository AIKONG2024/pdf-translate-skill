# Setup

## Required

- Python 3.11 or newer.
- Official `pdf2zh` CLI from PDFMathTranslate.

## Optional Provider Keys

Default service is `google`, which does not need an API key but still sends extracted text to a cloud provider.

Set only the keys for providers you choose:

| Provider | Environment variables |
| --- | --- |
| DeepL | `DEEPL_AUTH_KEY` |
| OpenAI | `OPENAI_API_KEY`, optional `OPENAI_BASE_URL`, `OPENAI_MODEL` |
| Azure OpenAI | `AZURE_OPENAI_BASE_URL`, `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_MODEL` |
| Gemini | `GEMINI_API_KEY`, optional `GEMINI_MODEL` |
| Azure Translator | `AZURE_ENDPOINT`, `AZURE_API_KEY` |
| Dify | `DIFY_API_URL`, `DIFY_API_KEY` |
| AnythingLLM | `AnythingLLM_URL`, `AnythingLLM_APIKEY` |
| OpenAI-compatible | `OPENAILIKED_BASE_URL`, `OPENAILIKED_API_KEY`, `OPENAILIKED_MODEL` |
| Ollama | `OLLAMA_HOST`, `OLLAMA_MODEL` |

## Credential Resolution

1. Use existing environment variables if present.
2. Use the agent's own secret vault if configured.
3. Ask the user for the required variable names.
4. Do not invent fallback services just because a key is missing.

## Smoke Test

```bash
pdf2zh --help
python pdf-translate/scripts/pdf_translate.py input.pdf --source en --target fr --service google --confirm-cloud --out outputs/pdf_translate
```
