.PHONY: setup
setup:
	@command -v uv >/dev/null 2>&1 || { \
		echo "Installing uv..."; \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
	}
	@echo "Setting up Python environment..."
	uv sync

.PHONY: install
install:
	@echo "Creating fresh environment and installing dependencies..."
	rm -rf .venv
	uv sync

.PHONY: fix
fix:
	@echo "Running ruff check and format..."
	uv run ruff check --fix .
	uv run ruff format .
