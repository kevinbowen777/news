from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse  # noqa:F401

from ..models import Article, Comment


class ArticleTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="johndoe",
            email="johndoe@example.com",
            password="secret",
        )

        self.article = Article.objects.create(
            title="A good title",
            body="Nice body content",
            author=self.user,
        )

    def test___str__(self):
        assert self.article.__str__() == self.article.title
        assert str(self.article) == self.article.title

    def test_article_content(self):
        self.assertEqual(f"{self.article.title}", "A good title")
        self.assertEqual(f"{self.article.author}", "johndoe")
        self.assertEqual(f"{self.article.body}", "Nice body content")

    """
    def test_get_absolute_url(self):
        self.assertEqual(
            self.article.get_absolute_url(), "/articles/{self.article.id}/")
        # self.assertEqual(self.article.get_absolute_url(), "/articles/1/")

    def test_article_detail_view(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.get("/articles/{self.article.id}/")
        # no_response = self.client.get("articles/100000/")
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "articles/article_detail.html")
    """

    def test_article_create_view(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.post(
            reverse("article_new"),
            {
                "title": "New title",
                "body": "New text",
                "author": self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Article.objects.last().title, "A good title")
        self.assertEqual(Article.objects.last().body, "Nice body content")

    def test_article_update_view(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.post(
            reverse("article_edit", args={self.article.id}),
            {
                "title": "Updated title",
                "body": "Updated text",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Article.objects.last().title, "Updated title")

    def test_article_delete_view(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.post(
            reverse("article_delete", args={self.article.id})
        )
        # response = self.client.get(reverse("article_delete", args="1"))
        self.assertEqual(response.status_code, 302)


class CommentTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="johndoe",
            email="johndoe@example.com",
            password="secret",
        )

        self.article = Article.objects.create(
            title="A good title",
            body="Nice body content",
            author=self.user,
        )

        self.comment = Comment.objects.create(
            article=self.article,
            comment="This is a comment",
            author=self.user,
        )

    def test_comment_create_view(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.post(
            reverse("comment_new", args={self.comment.id}),
            {
                "comment": "This is a comment",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comment.objects.first().comment, "This is a comment")
        self.assertTrue(self.comment.author == self.user)

    def test_comment_update(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.post(
            reverse("comment_edit", args={self.comment.id}),
            {
                "comment": "Updated comment",
            },
        )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(Comment.objects.first().comment, "Updated comment")

    def test_comment_delete(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.post(
            reverse("comment_delete", args={self.comment.id}),
        )
        self.assertEqual(response.status_code, 302)
        # self.assertNotContains(Message.objects.all().text, "Updated title")

    def test___str__(self):
        assert self.comment.__str__() == self.comment.comment
        assert str(self.comment) == self.comment.comment

    def test_get_absolute_url(self):
        self.assertEqual(self.comment.get_absolute_url(), "/articles/")
