import pytest
from django.test import Client, RequestFactory

from accounts.tests.factories import UserFactory
from articles.models import Article
from articles.tests.factories import ArticleFactory, CommentFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def request_factory():
    return RequestFactory()


@pytest.fixture
def article():
    return ArticleFactory()


@pytest.fixture
def comment():
    return CommentFactory()


@pytest.fixture
def client():
    return Client()


# Create articles for pagination tests
@pytest.fixture
def ten_articles(user):
    articles = []
    for article_id in range(10):
        article_id += 1
        Article.objects.create(
            title="A Tiny Test Article {0}".format(article_id),
            tags="dummy, test, django",
            # slug="2023/9/18/a-tiny-test-article-{0}/".format(article_id),
            body="Some article content {0}".format(article_id),
            author=user,
        )
        articles.append(article)
    return articles
