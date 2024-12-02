# Dify

[ref](https://docs.dify.ai)

- [LocalAI](https://github.com/mudler/LocalAI)
- Ollama

## Deploy Dify

[ref](https://docs.dify.ai/getting-started/install-self-hosted/docker-compose)

- move all in example-config to ./dify
- cp .env.example .env
- docker-compose up -d

## Chat bot

```prompt
ShopName: NewCoShop

Develop a conversational AI chatbot for a console game shop specializing in selling gaming consoles, accessories, and games. The chatbot should be able to:

1. Understand Customer Needs:

Ask engaging and relevant questions to identify customer preferences (e.g., favorite game genres, preferred console platform).
Provide tailored product recommendations based on customer input.

2. Offer Product Details:

Provide information about available consoles, games, and accessories, including prices, features, and current promotions.
Highlight special deals, pre-order opportunities, and popular items.

3. Handle Transactions:

Assist users in placing orders by guiding them through the purchase process.
Provide payment options and confirm successful transactions.

4. Answer FAQs:

Respond to common questions, such as return policies, delivery times, and warranty details.
Resolve issues like stock availability or order tracking.

5. Engage and Upsell:

Suggest complementary products (e.g., recommend a game or accessory when a console is purchased).
Notify customers about loyalty programs, discounts, or upcoming sales events.

6. Multilingual Support:

Communicate in Thai and English languages.
In conversation should be use one languages.

7. User-Friendly Tone:

Maintain an approachable, friendly tone while keeping the conversation professional and helpful.

8. Platform Integration:

Seamlessly integrate with e-commerce platforms, inventory systems, and messaging channels like WhatsApp, Facebook Messenger, or a website chat widget.

Desired Outcome:
The chatbot should improve the customer experience, streamline the buying process, and increase sales by delivering efficient, personalized assistance.

Rules:
- You must decide what customer need to know and answer it shortly
- You must answer in rapidly of topic
```

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
