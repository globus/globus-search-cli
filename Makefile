PYTHON_VERSION?=python2.7
VIRTUALENV=.venv_$(PYTHON_VERSION)
CLI_VERSION=$(shell grep '^__version__' globus_search_cli/version.py | cut -d '"' -f2)

.PHONY: develop build upload clean help

help:
	@echo "These are our make targets and what they do."
	@echo "All unlisted targets are internal."
	@echo ""
	@echo "  help:      Show this helptext"
	@echo "  build:     Create distributions to upload to pypi"
	@echo "  develop:   Create and install to local virtualenv"
	@echo "  release:   [build], but also upload to pypi using twine, git signed tag with version"
	@echo "  clean:     Remove typically unwanted files, mostly from [build]"


$(VIRTUALENV):
	virtualenv --python=$(PYTHON_VERSION) $(VIRTUALENV)
	$(VIRTUALENV)/bin/pip install -U twine pip setuptools
	$(VIRTUALENV)/bin/python setup.py develop

build: $(VIRTUALENV)
	$(VIRTUALENV)/bin/python setup.py sdist bdist_egg

release: $(VIRTUALENV) build
	git tag -s "$(CLI_VERSION)" -m "v$(CLI_VERSION)"
	$(VIRTUALENV)/bin/twine upload dist/*

.venv-lint:
	python3 -m venv .venv-lint
	.venv-lint/bin/pip install -q 'pre-commit==1.18'
.PHONY: lint
lint: .venv-lint
	.venv-lint/bin/pre-commit run --all-files --show-diff-on-failure

develop: $(VIRTUALENV)


clean:
	find -name '*.pyc' -delete
	-rm -r .venv*
	-rm -r build
	-rm -r dist
	-rm -r *.egg-info
