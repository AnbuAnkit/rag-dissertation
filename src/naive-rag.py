from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

Settings.llm = Ollama(model="gemma4:e4b", temperature=0)
Settings.embed_model = OllamaEmbedding(model_name="qwen3-embedding:0.6b")
Settings.chunk_size_limit = 512
Settings.chunk_overlap = 50

print(1)
