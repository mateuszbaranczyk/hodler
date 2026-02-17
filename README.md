## Getting Started

### Initial Setup

Install dependencies and create the virtual environment:

```bash
make setup
```

This will install `uv` (if not already installed) and set up the Python environment.

### Fresh Install

To create a fresh environment from scratch:

```bash
make install
```

This removes the existing `.venv` and reinstalls all dependencies.

### Activate Environment

```bash
source .venv/bin/activate
```

Or run commands directly without activating:

```bash
uv run python script.py
uv run pytest
```

## Adding Dependencies

### Using uv add (Recommended)

Add a production dependency:

```bash
uv add requests
uv add "pandas>=2.0.0"
```

Add a development dependency:

```bash
uv add --dev pytest
uv add --dev "black>=23.0.0"
```

### Manual Edit

Alternatively, edit `pyproject.toml` and add to the `dependencies` array:

```toml
[project]
dependencies = [
    "requests>=2.31.0",
    "pandas>=2.0.0",
]
```

For development dependencies, add to `[project.optional-dependencies]` dev section:

```toml
[project.optional-dependencies]
dev = [
    "ruff>=0.8.0",
    "pytest>=7.0.0",
]
```

Then run:

```bash
uv sync
```

## Using Ruff

Ruff is configured for linting and formatting with automatic import sorting.

### Fix and Format Code

```bash
make fix
```

This runs both linting fixes and formatting in one command.

### Manual Commands

Check code:

```bash
uv run ruff check .
```

Fix issues automatically:

```bash
uv run ruff check --fix .
```

Format code:

```bash
uv run ruff format .
```
