.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. image:: https://readthedocs.org/projects/globus-search-cli/badge/?version=latest
    :target: https://globus-search-cli.readthedocs.io/en/latest/?badge=latest

Globus Search CLI
=================

A command-line tool for interacting with Globus Search.

Provides the `globus-search` command.

.. note::
    At a future date, we hope to incorporate this functionality into the
    ``globus-cli``. At that time, support for this tool will be dropped.

Requirements
------------

You must have Python 3.5+ and ``pip`` installed.
There are no other requirements.

Install
-------

.. code-block:: bash

    pip install globus-search-cli

Install for Production Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you plan to use ``globus-search-cli`` in a production environment or
workflow, it is strongly recommended that you pin the exact version you are
using while it is in beta.

For example,

.. code-block:: bash

    pip install 'globus-search-cli==0.4.0'

Use
---

.. code-block:: bash

    globus-search --help

Uninstall
---------

.. code-block:: bash

    pip uninstall globus-search-cli

Bugs, Feature Requests, and Issues
----------------------------------

All issue tracking is done in the open
`Globus Search CLI <https://github.com/globus/globus-search-cli/issues/>`_
issue tracker.
