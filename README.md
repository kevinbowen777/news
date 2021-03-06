## news - A mini blog

news is a demonstration of basic Django functionality.


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
 - `docker-compose up --build`
 - `docker-compose exec web python manage.py migrate`
 - `docker-compose exec web python manage.py createsuperuser`
 - Open browser to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/

### Live Demo on Heroku:
 - [Newspaper app](https://limitless-crag-45588.herokuapp.com/)
### Docker Container Image:

 - TBD
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
