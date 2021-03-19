CHANGELOG
=========

Unreleased
----------

.. changelog:: 0.7.0 beta

* Add ``globus-search index role create`` command

* Add ``globus-search index role delete`` command

* Remove ``globus-search show-index``

.. changelog:: 0.6.0 beta

* Remove ``globus-search query-template`` commands and ``--query-template``
  option from ``globus-search query``

* Rename ``globus-search show-index`` to ``globus-search index show``

  * ``show-index`` is being kep for one version only, but it is deprecated and
    hidden from ``globus-search --help`` output

* Add ``globus-search index list`` to list indices where you have permissions

* Add ``globus-search index role list`` to list roles on an index (requires that
  you have admin)

.. changelog:: 0.5.2 beta

* Fix :issue:`4`, in which ``globus-search ingest`` did not properly handle
  ``--source-type=gmetalist``. Thanks to :user:`lukaszlacinski` for reporting
  this!

.. changelog:: 0.5.1 beta

* By default, output UTF-8 data without using ``\u...`` escapes

* ascii-only data can be obtained by setting the environment variable,
  ``GLOBUS_SEARCH_ENSURE_ASCII=1``

.. changelog:: 0.5.0 beta

* Add support for delete-by-query

.. changelog:: 0.4.1 beta

* Fix :issue:`3`, a bug with unauthenticated commands crashing before
  producing an unauthenticated client

.. changelog:: 0.4.0 beta

* The order of keys in JSON output will be sorted to remain stable

* Add ``--advanced`` and ``--bypass-visible-to`` flags to the query command

.. changelog:: 0.3.0 alpha

* Add the changelog

* Add a ReadTheDocs documentation site

* Remove support for python2

* Switch token storage from config file to a sqlite DB in the user's home
  directory. This will require users to re-login.

.. changelog:: 0.2.4 alpha

* Add support for setting a custom base URL (useful for testing)

* Add support for Integration environment

.. changelog:: 0.2.3 alpha

* Bugfix for token revocation on logout

.. changelog:: 0.2.2 alpha

* Switch to using SDK methods for task commands

.. changelog:: 0.2.1 alpha

* Add show-index and task list commands

* Autoformat all search-cli code

.. changelog:: 0.2.0 alpha

* Fix :issue:`1`, a bug with unauthenticated commands

.. changelog:: 0.1.0 alpha

* Initial release
