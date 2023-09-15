from datetime import datetime as dt

import factory
import factory.fuzzy
from django.template.defaultfilters import slugify

from accounts.tests.factories import UserFactory

from ..models import Article


class ArticleFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText(length=12, prefix="Breaking News: ")
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    body = factory.fuzzy.FuzzyText(length=50)
    publish = dt.now()
    author = factory.SubFactory(UserFactory)
    status = "PB"

    class Meta:
        model = Article
