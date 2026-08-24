install:
	python -m pip install -e ".[dev]"

test:
	pytest -q

run:
	uvicorn grc_analysis_engine.api.app:app --reload
