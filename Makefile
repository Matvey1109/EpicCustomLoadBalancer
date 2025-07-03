install-requirements:
	uv sync --frozen --no-install-project

start:
	uv venv
	$(MAKE) install-requirements

run_dummy_1:
	uvicorn dummy_backend:app --host 0.0.0.0 --port 8001

run_dummy_2:
	uvicorn dummy_backend:app --host 0.0.0.0 --port 8002

run_balancer:
	uvicorn app.main:app --host 0.0.0.0 --port 8000
