act:
	source .venv/bin/activate

setup:
	python -m venv .venv
	pip install uvicorn
	mkdir models
	source .venv

i: install
install:
	python -m pip install -r requirements.txt

f: freeze
freeze:
	python -m pip freeze > requirements.txt

c: clean
clean:
	pip freeze | while read p; do pip uninstall -y "$p"; done

dev:
	streamlit run main.py

serve:
	ollama serve

model:
	ollama run llama2

# test@gmail.com
docker.ui:
	docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main

docker.serve:
	docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

docker.model:
	docker exec -it ollama ollama run llama2
