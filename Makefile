install:
	bash .devcontainer/setup.sh

api:
	uvicorn api.main:app --reload --port 8000

ui:
	streamlit run ui/app.py --server.port 8501

gradio:
	python ui/app.py

test:
	pytest tests/ -v

format:
	black .

clean:
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	find . -type d -name '.pytest_cache' -prune -exec rm -rf {} +
