.. _`changelog`:

=========
Changelog
=========

``news`` issues are filed on `GitHub <https://github.com/kevinbowen777/news/issues>`_, and each ticket number here corresponds to a closed GitHub issue.

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

This project uses `towncrier <https://towncrier.readthedocs.io/>`_ for keeping
the changelog. DO NOT commit any changes to this file.

Backward incompatible (breaking) changes should only be introduced in major versions
with advance notice in the **Deprecations** section of releases.


..
    You should *NOT* be adding new change log entries to this file, this
    file is managed by towncrier. You *may* edit previous change logs to
    fix problems like typo corrections or such.
    To add a new change log entry, please see
    https://pip.pypa.io/en/latest/development/contributing/#news-entries
    but note that in toolbox the "news/" directory is named "changelog/".

.. towncrier release notes start

news 0.3.5 (2026-08-18)
=======================

Improved documentation
----------------------

-  (`#619 <https://github.com/kevinbowen777/news/619>`_): Add towncrier 25.8.0.


New features
------------

-  (`#642 <https://github.com/kevinbowen777/news/642>`_): Upgrade to Django 6.0.8

news 0.3.4 (2026-07-31)
=======================

Contributor-facing changes
--------------------------

- : Add Python 3.14 support.

-  (`#636 <https://github.com/kevinbowen777/news/636>`_): Update with Python 3.14.6 & 3.13.14.

-  (`#638 <https://github.com/kevinbowen777/news/638>`_): Rename default branch to main.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#632 <https://github.com/kevinbowen777/news/632>`_): Drop support for Python 3.11.


New features
------------

-  (`#601 <https://github.com/kevinbowen777/news/601>`_): Upgrade Django to 6.0.7.

news 0.3.3 (2025-05-05)
=======================

Contributor-facing changes
--------------------------

-  (`#548 <https://github.com/kevinbowen777/news/548>`_): Update Poetry to 2.1.2.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#544 <https://github.com/kevinbowen777/news/544>`_): Drop Python 3.10 support.


Improved documentation
----------------------

-  (`#543 <https://github.com/kevinbowen777/news/543>`_): Update Sphinx to 8.2.3.


New features
------------

-  (`#549 <https://github.com/kevinbowen777/news/549>`_): Upgrade Django to 5.2.


Security updated
----------------

-  (`#552 <https://github.com/kevinbowen777/news/552>`_): Replace safety package with pip-audit.

news 0.3.2 (2025-01-19)
=======================

Contributor-facing changes
--------------------------

-  (`#486 <https://github.com/kevinbowen777/news/486>`_): Add support for Python 3.13

-  (`#526 <https://github.com/kevinbowen777/news/526>`_): Re-build pyproject for Poetry 2.0.


New features
------------

-  (`#518 <https://github.com/kevinbowen777/news/518>`_): Upgrade Django to 5.1.4

news 0.3.0 (2023-12-30)
=======================

Contributor-facing changes
--------------------------

-  (`#209 <https://github.com/kevinbowen777/news/209>`_): Migrate to non-root Docker user & venv.

-  (`#388 <https://github.com/kevinbowen777/news/388>`_): Upgrade Poetry to 1.7.1.

-  (`#400 <https://github.com/kevinbowen777/news/400>`_): Update Python to 3.12.1.


Deprecations (removal in next major release)
--------------------------------------------

- : Drop support for Python 3.9.


Improved documentation
----------------------

- : Update Sphinx theme to Furo


New features
------------

-  (`#396 <https://github.com/kevinbowen777/news/396>`_): Upgrade to Django 5.0.

news 0.2.0 (2023-05-05)
=======================

New features
------------

-  (`#206 <https://github.com/kevinbowen777/news/206>`_): Upgrade to Django 4.2.

news 0.1.0 (2023-05-02)
=======================

Contributor-facing changes
--------------------------

- : Implement nox for testing

- : Mirror to GitLab.

-  (`#206 <https://github.com/kevinbowen777/news/206>`_): Migrate from SQLite to PostgreSQL

-  (`#221 <https://github.com/kevinbowen777/news/221>`_): Install ruff. Drop flake8-* packages.

-  (`#229 <https://github.com/kevinbowen777/news/229>`_): Upgrade PostgreSQL to 15.2


Improved documentation
----------------------

- : Add Sphinx for documentation

news 0.0.1 (2022-02-25)
=======================

Contributor-facing changes
--------------------------

- : Add support for Python 3.10

-  (`#10 <https://github.com/kevinbowen777/news/10>`_): Migrate from pipenv to Poetry


New features
------------

- : Support Django 4.0.4

-  (`#13 <https://github.com/kevinbowen777/news/13>`_): Build Docker support for Heroku deployment.


Miscellaneous internal changes
------------------------------

- : Initial commit
