init:
	pip install -r requirements.txt

test:
	py.test tests

all:
	pip install -r requirements.txt
	py.test tests

.PHONY: init tests all
