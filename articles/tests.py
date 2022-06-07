from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse  # noqa:F401

from .models import Article


class ArticleTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="johndoe",
            email="johndoe.example.com",
            password="secret",
        )

        self.article = Article.objects.create(
            title="A good title",
            body="Nice body content",
            author=self.user,
        )

    def test_string_representation(self):
        article = Article(title="A sample title")
        self.assertEqual(str(article), article.title)

    def test_article_content(self):
        self.assertEqual(f"{self.article.title}", "A good title")
        self.assertEqual(f"{self.article.author}", "johndoe")
        self.assertEqual(f"{self.article.body}", "Nice body content")


"""
    def test_get_absolute_url(self):
        self.assertEqual(self.article.get_absolute_url(), "/articles/1/")

    def test_article_detail_view(self):
        response = self.client.get("/articles/1/")
        no_response = self.client.get("articles/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "articles/article_detail.html")

    def test_article_create_view(self):
        response = self.client.article(
            reverse("article_new"),
            {
                "title": "New title",
                "body": "New text",
                "author": self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Article.objects.last().title, "New title")
        self.assertEqual(Article.objects.last().body, "New text")

    def test_article_update_view(self):
        response = self.client.article(
            reverse("article_edit", args="1"),
            {
                "title": "Updated title",
                "body": "Updated text",
            },
        )
        self.assertEqual(response.status_code, 302)

    def test_article_delete_view(self):
        response = self.client.article(reverse("article_delete", args="1"))
        self.assertEqual(response.status_code, 302)
"""
