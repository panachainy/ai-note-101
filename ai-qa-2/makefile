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
