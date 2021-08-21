.PHONY: typehint
typehint:
	mypy praudio

.PHONY: test
test:
	coverage run --source ./praudio -m pytest --verbose
	coverage report

.PHONY: lint
lint:
	pylint praudio

.PHONY: checklist
checklist: lint typehint test

.PHONY: install_dev
install_dev:
	pip install -e .[testing]

.PHONY: install
install:
	pip install .

.PHONY: clean
clean:
	find . -type f -name "*.pyc" | xargs rm -fr
	find . -type d -name __pycache__ | xargs rm -fr
