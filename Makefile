.PHONY: test env-reset env-reenter env-shell

# To run a single test file, use: pytest -vv tests/test_api.tavern.yaml
test:
	venv311/bin/python -m pytest -vv $(shell find tests -name '*.tavern.yaml') --tb=short

env-reset:
	@echo "Removing and rebuilding virtualenv..."
	rm -rf venv311
	python3 -m venv venv311
	source venv311/bin/activate && pip install -r requirements.txt
	@echo "Virtualenv reset complete."

env-reenter:
	@echo "Re-entering virtualenv..."
	@source venv311/bin/activate && echo "Virtualenv activated."

env-shell:
	@echo "Spawning shell with virtualenv activated..."
	@/bin/zsh -i -c "source venv311/bin/activate && exec /bin/zsh"
