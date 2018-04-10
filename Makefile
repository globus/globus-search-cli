PYTHON_VERSION?=python2.7
VIRTUALENV=.venv_$(PYTHON_VERSION)

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

develop: $(VIRTUALENV)/bin/globus-search


clean:
	find -name '*.pyc' -delete
	-rm -r $(VIRTUALENV)
	-rm -r build
	-rm -r dist
	-rm -r *.egg-info
