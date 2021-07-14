TiaC Systems Network (TSN) theme for Sphinx
===========================================

This repository contains the `Sphinx theme`_ for TiaC Systems Network (TSN)
documentation, based on `Read The Docs`_' default theme (sphinx_rtd_theme_).
This theme was forked from the Nordic Semiconductor NCS theme for Sphinx
(sphinx-ncs-theme_), which is also MIT licensed.
Copyright (c) 2021 Nordic Semiconductor ASA.

Installation
------------

This theme is distributed on PyPI as sphinx-tsn-theme_ and can be installed
with ``pip``:

.. code-block:: console

    pip install sphinx-tsn-theme

Usage
-----

To use the theme in your Sphinx project, you will need to add the following to
your ``conf.py`` file:

.. code-block:: python

    html_theme = "sphinx_tsn_theme"

Releasing
---------

1. Make sure you have a PyPI account and access to https://pypi.org/project/sphinx-tsn-theme/.
2. Make sure all your changes have been commited to the ``main`` branch.
3. Add a commit which updates the version number in ``sphinx_tsn_theme/__init__.py``.
4. Tag this commit with the version number, e.g. ``git tag -a 2020.4 -m "version 2020.4"``.
5. Push the commit and the tag to the ``main`` branch.
6. `Generate the source and binary distributions with setup.py <https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives>`__.
7. `Upload the two files from step 6 to PyPI with twine <https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives>`__.

.. _Sphinx theme: https://www.sphinx-doc.org/en/master/usage/theming.html
.. _Read The Docs: https://readthedocs.org/
.. _sphinx_rtd_theme: https://github.com/readthedocs/sphinx_rtd_theme
.. _sphinx-ncs-theme: https://github.com/nrfconnect/doc-sphinx-ncs-theme
.. _sphinx-tsn-theme: https://pypi.org/project/sphinx-tsn-theme/
