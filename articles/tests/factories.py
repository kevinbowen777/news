from datetime import datetime as dt

import factory
import factory.fuzzy
from django.template.defaultfilters import slugify

from accounts.tests.factories import UserFactory

from ..models import Article, Comment


class ArticleFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText(length=12, prefix="Breaking News: ")
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    body = factory.fuzzy.FuzzyText(length=50)
    publish = dt.now()
    author = factory.SubFactory(UserFactory)
    tags = "testing, django, example, greatarticle"
    status = "PB"

    class Meta:
        model = Article


class CommentFactory(factory.django.DjangoModelFactory):
    article = factory.SubFactory(ArticleFactory)
    name = factory.SubFactory(UserFactory)
    email = "test_dummy@example.com"
    # email = f"{name.username}@example.com"
    body = factory.fuzzy.FuzzyText(length=50)

    class Meta:
        model = Comment
