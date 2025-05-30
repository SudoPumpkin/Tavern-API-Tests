.PHONY: test python env-reset env-reenter env-shell

# Run all Tavern tests
test:
	venv311/bin/python -m pytest -vv $(shell find tests -name '*.tavern.yaml') --tb=short

# Run all Python test scripts (not using pytest, just raw execution)
python:
	@echo "Running all Python test scripts..."
	@for file in $(shell find tests -name '*.py'); do \
		echo "� Running $$file"; \
		venv311/bin/python $$file; \
		echo ""; \
	done

# Rebuild virtual environment
env-reset:
	@echo "Removing and rebuilding virtualenv..."
	rm -rf venv311
	python3 -m venv venv311
	source venv311/bin/activate && pip install -r requirements.txt
	@echo "Virtualenv reset complete."

# Re-enter virtual environment
env-reenter:
	@echo "Re-entering virtualenv..."
	@source venv311/bin/activate && echo "Virtualenv activated."

# Spawn a shell with virtualenv activated
env-shell:
	@echo "Spawning shell with virtualenv activated..."
	@/bin/zsh -i -c "source venv311/bin/activate && exec /bin/zsh"
