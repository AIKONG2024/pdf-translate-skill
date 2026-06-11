# Services

## Default

Use `google` when the user does not specify a service. Google does not require an API key, but it is still a cloud service and requires explicit user confirmation before running.

## Cloud Services

These services may send extracted PDF text to an external provider:

| Service | Required setup |
| --- | --- |
| `google` | None |
| `bing` | None |
| `deepl` | `DEEPL_AUTH_KEY` |
| `deeplx` | `DEEPLX_ENDPOINT` |
| `openai` | `OPENAI_API_KEY`, optionally `OPENAI_BASE_URL`, `OPENAI_MODEL` |
| `azure-openai` | `AZURE_OPENAI_BASE_URL`, `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_MODEL` |
| `gemini` | `GEMINI_API_KEY`, optionally `GEMINI_MODEL` |
| `azure` | `AZURE_ENDPOINT`, `AZURE_API_KEY` |
| `tencent` | `TENCENTCLOUD_SECRET_ID`, `TENCENTCLOUD_SECRET_KEY` |
| `dify` | `DIFY_API_URL`, `DIFY_API_KEY` |
| `anythingllm` | `AnythingLLM_URL`, `AnythingLLM_APIKEY` |
| `openailiked` | `OPENAILIKED_BASE_URL`, `OPENAILIKED_API_KEY`, `OPENAILIKED_MODEL` |

Before any cloud service runs, get explicit user confirmation.

## Local Options

| Service | Required setup |
| --- | --- |
| `ollama` | `OLLAMA_HOST`, `OLLAMA_MODEL` |
| `argos` | Argos Translate language packages |

Local options still need setup validation, but they do not need the cloud-transfer confirmation.

## Language Codes

Use provider-compatible short codes such as `en`, `fr`, `de`, `es`, `ja`, `ko`, and `zh`. Provider support is service-specific, so do not present a fixed language-pair list as exhaustive.

