setup:
	# python -m venv .venv
	pip install uvicorn
	# pip install pipreqs
	# pip install pipreqsnb
	# source .venv/bin/activate

gen_dependency:
	# pipreqs .
	# pipreqsnb .

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
	uvicorn main:app --reload --host 0.0.0.0 --port 5000
	# uvicorn main:app --reload --port 5000
