CHANGELOG
=========

Unreleased
----------

* The order of keys in JSON output will be sorted to remain stable

0.3.0
-----

* Add the changelog

* Add a ReadTheDocs documentation site

* Remove support for python2

* Switch token storage from config file to a sqlite DB in the user's home
  directory. This will require users to re-login.

0.2.4
-----

* Add support for setting a custom base URL (useful for testing)

* Add support for Integration environment

0.2.3
-----

* Bugfix for token revocation on logout

0.2.2
-----

* Switch to using SDK methods for task commands

0.2.1
-----

* Add show-index and task list commands

* Autoformat all search-cli code

0.2.0
-----

* Fix :issue:`1`, a bug with unauthenticated commands

0.1.0
-----

* Initial release
