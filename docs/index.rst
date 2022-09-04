news - A Django news application
================================

.. toctree::
   :hidden:
   :maxdepth: 1

   license

This repository runs a Django 4.1 news application.

Features
--------

 * Create, edit, and delete posts
 * User registration with email verification & social(GitHub) login
 * Bootstrap4 & crispy-forms decorations
 * Customizable user profiles with bio, profile picture & country flags
 * Nox testing sessions (black, linting, pytest, coverage, Sphinx doc generation)

Installation
------------

To install the news project,
run this command in your terminal:

.. code-block:: console

   $ git clone https://github.com/kevinbowen777/news.git
   $ cd news

Local install:
--------------

.. code-block:: console

   $ poetry shell
   $ poetry install
   $ python manage.py migrate
   $ python manage.py createsuperuser


Docker install:
---------------

.. code-block:: console

   $ docker-compose up --build
   $ docker-compose python manage.py migrate
   $ docker-compose python manage.py createsuperuser


Usage
-----

To run news, locally, enter the following on the command line:

.. code-block:: console

   $ python manage.py runserver

For both local, or Docker installations, browse to `<http://127.0.0.1:8000>`_ or `<http://127.0.0.1:8000/admin/>`_

Testing
-------

.. code-block:: console

   $ python manage.py runserver
   $ docker-compose exec web python manage.py test
   $ coverage run -m pytest
   $ nox --list-sessions
   $ nox
   $ nox -rs lint-3.11
   $ nox -s tests

Live Application Demonstration on Heroku
----------------------------------------
`kbowen-django-news <https://kbowen-django-news.herokuapp.com/>`_

Reporting Bugs
--------------

Visit the news `Issues page <https://github.com/kevinbowen777/news/issues>`_ on GitHub.
