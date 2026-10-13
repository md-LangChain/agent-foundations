"""Centralized model initialization.

The notebook imports `model` from here, so swapping providers
(OpenAI / Anthropic / Azure / Bedrock) only requires editing this file.

Default: OpenAI through the LangSmith LLM Gateway. On assigned machines
`LC_GATEWAY_KEY` is a *service* key (different from `LANGSMITH_API_KEY`).
It is used as `OPENAI_API_KEY` against the gateway base URL — not a
platform.openai.com key.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Always load the workshop-root .env, regardless of Jupyter's working directory.
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env", override=True)

GATEWAY_OPENAI_BASE_URL = "https://gateway.smith.langchain.com/openai/v1"

gateway_key = os.environ.get("LC_GATEWAY_KEY")
if gateway_key:
    os.environ["OPENAI_API_KEY"] = gateway_key
    os.environ["OPENAI_BASE_URL"] = os.environ.get("OPENAI_BASE_URL") or GATEWAY_OPENAI_BASE_URL

from langchain_openai import ChatOpenAI

# ChatOpenAI reads OPENAI_API_KEY + OPENAI_BASE_URL from the environment.
model = ChatOpenAI(
    model="gpt-4.1-mini",
    use_responses_api=True,
)

# --- Anthropic via gateway (not currently supported on all machines) ---
# model = init_chat_model("anthropic:claude-sonnet-5")

# --- Azure OpenAI ---
# from langchain_openai import AzureChatOpenAI
# model = AzureChatOpenAI(azure_deployment="gpt-5.6-terra", streaming=True)

# --- AWS Bedrock ---
# from langchain_aws import ChatBedrockConverse
# model = ChatBedrockConverse(
#     provider="anthropic",
#     model_id="anthropic.claude-sonnet-4-20250514-v1:0",
# )
