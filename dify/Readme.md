# Dify

[ref](https://docs.dify.ai)

- [LocalAI](https://github.com/mudler/LocalAI)
- Ollama

## Run

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

## access localhost from docker

- Ollama `http://host.docker.internal:11434`
- LocalAI `http://host.docker.internal:8080`

## Model

- Chat - llama3.2
- Rerank - cross-encoder
