act:
	source .venv/bin/activate

setup:
	python -m venv .venv
	bun i
	make act

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
	bun run dev
	# streamlit run main.py
