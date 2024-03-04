env.act:
	source .venv/bin/activate

f: freeze
freeze: env.export
env.export:
	python -m pip freeze > requirements.txt

re: env.recreate
env.recreate:
	python -m venv .venv

setup:
	make env.recreate
	make env.act

i: install
install:
	python -m pip install -r requirements.txt

c: clean
clean:
	pip freeze | while read p; do pip uninstall -y "$p"; done

dev:
	streamlit run main.py
