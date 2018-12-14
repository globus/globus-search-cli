PYTHON_VERSION?=python2.7
VIRTUALENV=.venv_$(PYTHON_VERSION)
AUTOF_VENV=.venv-autoformat
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

$(AUTOF_VENV):
	virtualenv --python python3 $(AUTOF_VENV)
	$(AUTOF_VENV)/bin/pip install -U 'pip==18.1' 'setuptools==40'
	$(AUTOF_VENV)/bin/pip install 'black==18.9b0' 'flake8-bugbear==18.8.0' 'flake8>=3.0,<4.0' 'isort>=4.3,<5.0'
	touch .venv-autoformat
autoformat: $(AUTOF_VENV)
	$(AUTOF_VENV)/bin/isort --recursive globus_search_cli/ setup.py
	$(AUTOF_VENV)/bin/black globus_search_cli/ setup.py


develop: $(VIRTUALENV)


clean:
	find -name '*.pyc' -delete
	-rm -r .venv_*
	-rm -r build
	-rm -r dist
	-rm -r *.egg-info
