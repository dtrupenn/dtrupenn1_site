#!/usr/bin/make -f

.PHONY: format

venv:
	python3 -m venv venv
	source venv/bin/activate

format:
	@if ! command -v black &> /dev/null; then \
	    echo "black formatter not found, please install it via pip!"; \
	    false; \
	fi;
	black config.py server.py

install:
	pip3 install -r requirements.txt
