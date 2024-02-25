setup:
	# pip install -r requirements.txt
	python -m venv venv
	pip install uvicorn

dev:
	uvicorn main:queue_prompt
	# uvicorn main:app --reload --port 5000
