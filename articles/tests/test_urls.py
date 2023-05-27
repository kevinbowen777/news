import pytest
from django.urls import resolve, reverse

from .factories import ArticleFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def article():
    return ArticleFactory()


def test_article_list_reverse():
    """article_list should reverse to /articles/."""
    assert reverse("article_list") == "/articles/"


def test_article_list_resolve():
    """/articles/" should resolve to article_list."""
    assert resolve("/articles/").view_name == "article_list"


def test_article_add_reverse():
    """article_new should reverse to /articles/new/."""
    assert reverse("article_new") == "/articles/new/"


def test_article_add_resolve():
    """/articles/new/" should resolve to article_new."""
    assert resolve("/articles/new/").view_name == "article_new"


# TODO Revisit ArticleFactory() construction & build an appropriate slug to test
"""
def test_article_detail_reverse(article):
    # article_detail should reverse to /articles/uuid.
    url = reverse("article_detail", kwargs={"pk": article.id})
    assert url == f"/articles/{article.id}/"


def test_article_detail_resolve(article):
    # /articles/{article.id}/ should resolve to article_detail.
    url = f"/articles/{article.id}/"
    assert resolve(url).view_name == "article_detail"
"""
