PYTHON_VERSION?=python2.7
VIRTUALENV=.venv_$(PYTHON_VERSION)
AUTOF_VENV=.venv-autoformat

.PHONY: develop build upload clean help

help:
	@echo "These are our make targets and what they do."
	@echo "All unlisted targets are internal."
	@echo ""
	@echo "  help:      Show this helptext"
	@echo "  build:     Create distributions to upload to pypi"
	@echo "  develop:   Create and install to local virtualenv"
	@echo "  upload:    [build], but also upload to pypi using twine"
	@echo "  clean:     Remove typically unwanted files, mostly from [build]"


$(VIRTUALENV):
	virtualenv --python=$(PYTHON_VERSION) $(VIRTUALENV)

build: $(VIRTUALENV)
	$(VIRTUALENV)/bin/python setup.py sdist bdist_egg

$(VIRTUALENV)/bin/twine: $(VIRTUALENV)
	$(VIRTUALENV)/bin/pip install -U twine
	touch $(VIRTUALENV)/bin/twine

upload: $(VIRTUALENV)/bin/twine build
	$(VIRTUALENV)/bin/twine upload dist/*

$(VIRTUALENV)/bin/globus-search: $(VIRTUALENV) setup.py globus_search_cli
	$(VIRTUALENV)/bin/python setup.py develop
	touch $(VIRTUALENV)/bin/globus-search

$(AUTOF_VENV):
	virtualenv --python python3 $(AUTOF_VENV)
	$(AUTOF_VENV)/bin/pip install -U 'pip==18.1' 'setuptools==40'
	$(AUTOF_VENV)/bin/pip install 'black==18.9b0' 'flake8-bugbear==18.8.0' 'flake8>=3.0,<4.0' 'isort>=4.3,<5.0'
	touch .venv-autoformat
autoformat: $(AUTOF_VENV)
	$(AUTOF_VENV)/bin/isort --recursive globus_search_cli/ setup.py
	$(AUTOF_VENV)/bin/black globus_search_cli/ setup.py


develop: $(VIRTUALENV)/bin/globus-search


clean:
	find -name '*.pyc' -delete
	-rm -r .venv_*
	-rm -r build
	-rm -r dist
	-rm -r *.egg-info
