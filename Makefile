.PHONY: web install clean

# Default target
all: web

# Run the Agent with ADK Web UI
web:
	@echo "Starting ADK Web UI..."
	# Run adk web pointing to the source directory where agents are located
	uv run adk web src

# Install dependencies from pyproject.toml
install:
	@echo "Installing dependencies..."
	uv sync

# Clean up cache files
clean:
	@echo "Cleaning up..."
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete