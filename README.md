## news 

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/news.svg)](https://github.com/kevinbowen777/news/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

news is a demonstration of basic Django functionality with a blog-like app.

---
## Features
 - User registration with email verification, password recovery
 - Support for social authentication via GitHub OAuth
 - Create, edit, and delete posts
 - Admin management of users and posts
 - django-debug-toolbar available in DEBUG mode

### Installation
 - `git clone https://github.com/kevinbowen777/news.git`
 - `cd news`
 - Local installation:
     - `poetry shell`
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation:
     - `docker-compose up --build`
     - `docker-compose python manage.py migrate`
     - `docker-compose python manage.py createsuperuser`
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/

### Live Demo on Heroku:
 - [Newspaper app](https://kbowen-django-news.herokuapp.com/)

---
## Screenshots
Home Page
![Homepage](https://github.com/kevinbowen777/news/blob/master/images/news_home-page.png)

Articles Page with drop-down menu shown
![Articles](https://github.com/kevinbowen777/news/blob/master/images/news_articles.png)

Login Page with GitHub Oauth option
![Login](https://github.com/kevinbowen777/news/blob/master/images/news_login.png)

---
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/kevinbowen777/news/blob/master/LICENSE)
---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/news/issues)
      to view currently open bug reports or open a new issue.
