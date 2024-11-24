# Dify

[ref](https://docs.dify.ai)

- [LocalAI](https://github.com/mudler/LocalAI)
- Ollama

## LocalAI

**Not work now**

Run

```sh
# CPU only image:
docker run -ti --name local-ai -p 8080:8080 localai/localai:latest-cpu

# Nvidia GPU:
docker run -ti --name local-ai -p 8080:8080 --gpus all localai/localai:latest-gpu-nvidia-cuda-12

# CPU and GPU image (bigger size):
docker run -ti --name local-ai -p 8080:8080 localai/localai:latest

# AIO images (it will pre-download a set of models ready for use, see https://localai.io/basics/container/)
docker run -ti --name local-ai -p 8080:8080 localai/localai:latest-aio-cpu
```

access `http://localhost:8080`

- Rerank - cross-encoder

    ```bash
    curl http://localhost:8080/v1/rerank \
      -H "Content-Type: application/json" \
      -d '{
      "model": "jina-reranker-v1-base-en",
      "query": "Organic skincare products for sensitive skin",
      "documents": [
        "Eco-friendly kitchenware for modern homes",
        "Biodegradable cleaning supplies for eco-conscious consumers",
        "Organic cotton baby clothes for sensitive skin",
        "Natural organic skincare range for sensitive skin",
        "Tech gadgets for smart homes: 2024 edition",
        "Sustainable gardening tools and compost solutions",
        "Sensitive skin-friendly facial cleansers and toners",
        "Organic food wraps and storage solutions",
        "All-natural pet food for dogs with allergies",
        "Yoga mats made from recycled materials"
      ],
      "top_n": 3
    }'
    ```

- LocalAI `http://host.docker.internal:8080/v1`



### Model config

Place dify/localai/models/xxxx.yaml

```yaml reranker.yaml
name: japanese-reranker
backend: rerankers
parameters:
  model: hotchpotch/japanese-reranker-cross-encoder-small-v1
```

## Ollama

- Ollama `http://host.docker.internal:11434`
- Chat - llama3.2
