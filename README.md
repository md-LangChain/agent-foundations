# Agent Foundations

A ~25 minute hands-on notebook: start with a standard LangChain agent (`create_agent`), then step into Deep Agents — sandbox, long-term memory, summarization, and subagents.

## What you'll build

1. A barebones agent — just a model
2. An `@tool` that calls OpenAI web search
3. An agent with tools
4. A single-turn search run
5. Deep Agents + sandbox (`execute`)
6. Deep Agents + long-term memory (`/memories/`)
7. Deep Agents + summarization
8. Deep Agents + subagents (`task()`)

## Setup

```bash
uv sync
cp .env.example .env
# fill in LANGSMITH_API_KEY and OPENAI_API_KEY
uv run jupyter notebook agent_foundations.ipynb
```

## Needs

- `LANGSMITH_API_KEY` — tracing and sandbox
- `OPENAI_API_KEY` — model calls

No Tavily key required.
