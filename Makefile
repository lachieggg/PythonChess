VENV := venv
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip

.PHONY: run ai setup clean

## Create venv and install dependencies
setup:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

## Run the game
run: $(VENV)/bin/activate
	$(PYTHON) Game.py

## Run AI vs AI mode (5 second delay between turns)
ai: $(VENV)/bin/activate
	$(PYTHON) Game.py --ai

## Remove venv
clean:
	rm -rf $(VENV)
