from datetime import datetime as dt

import pytest

pytestmark = pytest.mark.django_db


def test_article___str__(article):
    assert article.__str__() == article.title
    assert str(article) == article.title


def test_article_get_absolute_url(article):
    slug_time = dt.now().strftime("%Y/%-m/%-d")
    assert article.get_absolute_url() == f"/articles/{slug_time}/{article.slug}/"


def test_comment__str__(comment):
    assert comment.__str__() == f"Comment by {comment.name} on {comment.article}"
