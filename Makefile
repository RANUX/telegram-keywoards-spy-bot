# Makefile for AI Assistant

# Run the AI Assistant
run:
	source venv/bin/activate && python telegram_bot.py

# Install the required dependencies
install:
	python -m venv venv && source venv/bin/activate && pip install -r requirements.txt

# Clear the virtual environment
clear:
	rm -rf venv

build:
	docker build -t spybot .

.PHONY: run install clear