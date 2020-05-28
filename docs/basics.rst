Basic Usage
===========

The globus-search-cli provides a way of communicating with the Globus Search
service. Most of the ideas and concepts exposed by this tool are more fully
documented in the
`Globus Search Documentation <https://docs.globus.org/api/search/>`_.

Authentication: Login and Logout
--------------------------------

Globus Search does allow some operations to be performed without logging in.
However, for the vast majority of commands, and to have the ability to read
documents which are not public, you will need to log in.

To do so, simply

.. code-block:: bash

    globus-search login
    # and follow the prompts

You should never login on insecure or public machines. Tokens acquired from login
are stored in your home directory (only readable by your user).

.. note::
    Some other Globus applications provide sophisticated integrations with the
    user's browser. In the case of the globus-search-cli, login is *always*
    done via the text prompt for simplicity.

Logout is equally simple. Just

.. code-block:: bash

    globus-search logout


Ingest & Query
--------------

Some of the operations which you will want to perform are data ingest and
search queries.

These are provided through three commands:

* ``globus-search ingest``
* ``globus-search query``
* ``globus-search structured-query``

Ingest commands require that you provide JSON documents containing your data.
The formats supported are documented as part of the Search API documentation,
as
`GIngest documents <https://docs.globus.org/api/search/ingest/#gingest>`_
and
`GMetaList documents <https://docs.globus.org/api/search/ingest/#gmetalist>`_.

The ``query`` and ``structured-query`` commands correspond to the
`GET Query <https://docs.globus.org/api/search/search/#simple_get_query>`_ and
`POST QUERY <https://docs.globus.org/api/search/search/#complex_post_query>`_
operations. For ``structured-query`` calls, you will want to formulate a
`GSearchRequest document <https://docs.globus.org/api/search/search/#gsearchrequest>`_.
