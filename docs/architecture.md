# RAG Methods Architecture

The notebooks in this repository demonstrate components that can be combined into one request path. They are intentionally independent so each method can be studied and evaluated separately.

![RAG methods implemented](../assets/production-rag-methods.png)

## Recommended request flow

```text
User question
  -> semantic cache lookup
  -> rewrite conversational question when history is present
  -> generate query variants or a HyDE document when recall needs help
  -> retrieve candidates with dense, lexical, or hybrid search
  -> rerank candidates with a cross-encoder
  -> compress the selected context
  -> generate a grounded answer
  -> store the answer in the semantic cache when appropriate
```

Not every request needs every step. A production system should select methods based on measured value, latency budget, and the characteristics of its data.

## Method guide

| Method | Best use case | Trade-off |
| --- | --- | --- |
| Query rewriting | Follow-up questions and multi-turn chat | One extra model call |
| Multi-query retrieval | Ambiguous or broad questions | More retrieval work |
| HyDE | Sparse queries where wording differs from source documents | Can introduce a less faithful search representation |
| Hybrid search | Corpora with exact terms, IDs, and semantic language | Requires lexical and vector retrieval paths |
| Reranking | High-value answers where top-k precision matters | Adds cross-encoder latency |
| Contextual compression | Large retrieved passages or strict token budgets | May omit useful context if tuned aggressively |
| Semantic caching | Repeated or paraphrased questions | Needs threshold tuning to avoid false cache matches |

## VS Code workflow

Open the repository root in VS Code, then:

1. Run `uv sync` in the integrated terminal.
2. Install the Python and Jupyter extensions if VS Code prompts for them.
3. Open `notebooks/simple.ipynb` and select the `.venv` Python environment as the kernel.
4. Create `.env` from your local credentials and run the notebook cells in order.

For a LinkedIn screenshot, expand the `notebooks`, `assets`, and `docs` folders in Explorer, open `README.md`, and use the Markdown preview. The project tree and architecture graphic will be visible together in a single clean frame.
