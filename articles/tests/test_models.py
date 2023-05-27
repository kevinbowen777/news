from django.test import TestCase

from accounts.tests.factories import UserFactory

from .factories import ArticleFactory

# from ..models import Review


class ArticleTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.article = ArticleFactory()
        """
        self.review = Review.objects.create(
            article=self.article,
            creator=self.user,
            review="An excellent review",
        )
        """

    def test__str__(self):
        assert self.article.__str__() == self.article.title
        assert str(self.article) == self.article.title

    """
    def test_get_absolute_url(self):
        url = self.article.get_absolute_url()
        assert url == f"/articles/{self.article.id}/"

    def test_review__str__(self):
        assert self.review.__str__() == self.review.review
        assert str(self.review) == self.review.review

    def test_review_get_absolute_url(self):
        url = self.review.get_absolute_url()
        assert url == f'{"/articles/"}'
    """
