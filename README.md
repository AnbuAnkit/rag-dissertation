Hallucination Across Retrieval-Augmented Generation Strategies, a comparative study

>About

RAG is widely used to reduce LLM hallucination, but "RAG" covers very
different designs. This project compares four architectures from
Naive, Advanced, Modular and Agentic RAG and measures how each affects
hallucination rate and various other metrics

The generator LLM, embedding model, chunking strategy, temperature and base
prompt are held constant across all conditions, so differences in
hallucination can be attributed to the retrieval architecture itself.

>Setup

- Frameworks: LlamaIndex/Langchain
- Generator LLMs: `gemma4:e4b` via Ollama
- Embeddings models: `qwen3-embedding:0.6b` via Ollama or BGE-M3 (BAAI)
- Dataset fields: Medical | Science | General | Legal | Enterprise
- Evaluation frameworks: RAGAS/DeepEval

>Repository structure (Note: Models are not included in the repository)

| Path | Contents |
|---|---|
| `src/` | LlamaIndex implementation (`naive-rag.py` / `.ipynb`), plus `data/` and `preprocessing/` with the text corpus used for retrieval |
| `Datasets/sciQ/` | SciQ `train`, `validation` and `test` CSVs (question, correct answer, distractors, support passage) |
| `Literature/` | Reference papers on RAG surveys, RAG hallucination, comparative RAG evaluations, and domain applications (healthcare, legal, scientific) |
| `Literature Review.xlsx` | Structured literature review sheet |
| `Presentations/` | Progress presentations (August, September) and the intro deck |
| `Monthly report/` | Monthly progress reports (MPR) and dissertation title forms |

>Status

Work in progress.
