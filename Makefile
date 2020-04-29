PYTHON_VERSION?=python3
VIRTUALENV=.venv
CLI_VERSION=$(shell grep '^__version__' globus_search_cli/version.py | cut -d '"' -f2)

.PHONY: release clean help install

define HELPTEXT
These are our make targets and what they do.

help:      Show this helptext

install:   Build the globus-search CLI in a local virtualenv, and link it in the
           current directory.

clean:     Typical cleanup and uninstall

release:   [Maintainers Only] Release a new version to pypi
endef
help:
	@echo "$$HELPTEXT"

$(VIRTUALENV):
	virtualenv --python=$(PYTHON_VERSION) $(VIRTUALENV)
	$(VIRTUALENV)/bin/pip install -U pip setuptools
	$(VIRTUALENV)/bin/python setup.py develop

install: $(VIRTUALENV)
	$(VIRTUALENV)/bin/python setup.py develop
	-rm globus-search
	ln -s "$(VIRTUALENV)/bin/globus-search" globus-search

$(VIRTUALENV)/bin/twine: $(VIRTUALENV)
	$(VIRTUALENV)/bin/pip install -U twine
release: $(VIRTUALENV) $(VIRTUALENV)/bin/twine
	$(VIRTUALENV)/bin/python setup.py sdist bdist_egg
	git tag -s "$(CLI_VERSION)" -m "v$(CLI_VERSION)"
	$(VIRTUALENV)/bin/twine upload dist/*

clean:
	find -name '*.pyc' -delete
	-rm globus-search
	-rm -r .venv*
	-rm -r build
	-rm -r dist
	-rm -r *.egg-info
