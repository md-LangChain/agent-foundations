"""Centralized model initialization.

The notebook imports `model` from here, so swapping providers
(OpenAI / Anthropic / Azure / Bedrock) only requires editing this file.

Default: OpenAI via `OPENAI_API_KEY`.
"""

from pathlib import Path
from dotenv import load_dotenv

# Always load the workshop-root .env, regardless of Jupyter's working directory.
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env", override=True)

from langchain_openai import ChatOpenAI

# ChatOpenAI reads OPENAI_API_KEY from the environment.
model = ChatOpenAI(
    model="gpt-4.1-mini",
    use_responses_api=True,
)

# --- Anthropic ---
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
