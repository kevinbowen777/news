import datetime

import factory
import factory.fuzzy
import pytest
from django.template.defaultfilters import slugify

from accounts.tests.factories import UserFactory

from ..models import Article


@pytest.fixture
def article():
    return ArticleFactory()


class ArticleFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText(length=12, prefix="Breaking News: ")
    body = factory.fuzzy.FuzzyText(length=50)
    slug = slugify(title)
    publish = factory.fuzzy.FuzzyDate(datetime.date(2022, 6, 23))
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = Article
