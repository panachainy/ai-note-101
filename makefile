setup:
	# python -m venv .venv
	pip install uvicorn
	# source .venv/bin/activate

gen_dependency:
	pip install pipreqs
	pipreqs .

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
	uvicorn main:queue_prompt
	# uvicorn main:app --reload --port 5000
