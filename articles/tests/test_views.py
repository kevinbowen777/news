from datetime import datetime as dt

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

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
            slug="a-good-title",
            author=self.user,
        )

        self.article2 = Article.objects.create(
            title="A good second title",
            body="Nice body content for a second article",
            # slug="a-good-title",
            author=self.user,
            status="DF",
        )
        self.slug_time = dt.now().strftime("%Y/%-m/%-d")

    def test___str__(self):
        assert self.article.__str__() == self.article.title
        assert str(self.article) == self.article.title

    def test_article_content(self):
        self.assertEqual(f"{self.article.title}", "A good title")
        self.assertEqual(f"{self.article.slug}", "a-good-title")
        self.assertEqual(f"{self.article.author}", "johndoe")
        self.assertEqual(f"{self.article.body}", "Nice body content")
        self.assertEqual(f"{self.article.status}", "PB")

    def test_get_absolute_url(self):
        self.assertEqual(
            self.article.get_absolute_url(),
            f"/articles/{self.slug_time}/{self.article.slug}/",
        )

    def test_article_detail_view(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.get(f"/articles/{self.slug_time}/{self.article.slug}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "articles/article_detail.html")

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
        self.assertEqual(response.status_code, 200)
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
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(Article.objects.get(id=self.article.id).title, "Updated title")
        # self.assertEqual(Article.objects.first().title, "Updated title")

    def test_article_delete_view(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.post(reverse("article_delete", args={self.article.id}))
        # response = self.client.get(reverse("article_delete", args="1"))
        self.assertEqual(response.status_code, 302)


class ArticleListViewTest(TestCase):
    def setUp(self):
        url = reverse("article_list")
        self.response = self.client.get(url)

        self.user = get_user_model().objects.create_user(
            username="johndoe",
            email="johndoe@example.com",
            password="secret",
        )

        self.article = Article.objects.create(
            title="A good title",
            body="Nice body content",
            slug="a-good-title",
            author=self.user,
        )

        """
        # Create articles for pagination tests
        number_of_articles = 10
        for article_id in range(number_of_articles):
            Article.objects.create(
                title="A Tiny Test Article {0}".format(article_id),
                slug="2023/7/15/a-tiny-test-article-{0}/".format(article_id),
                body="Some article content {0}".format(article_id),
                author=self.user,
            )
        """

    def test_view_url_exists_at_desired_location(self):
        # response = self.client.get("/articles/")
        self.assertEqual(self.response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "articles/article_list.html")

    """
    def test_pagination_is_five(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTrue("is_paginated" in self.response.context)
        self.assertTrue(self.response.context["is_paginated"] is True)
        self.assertEqual(len(self.response.context["article_list"]), 5)

    def test_lists_all_articles(self):
        self.client.login(email="johndoe@example.com", password="secret")
        # Get second page and confirm it has (exactly) the remaining 3 items
        response = self.client.get("articles/?page=2")
        self.assertEqual(self.response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(self.response.context["is_paginated"] is True)
        self.assertEqual(len(self.response.context["article_list"]), 2)
    """


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
            slug="a-good-title",
            author=self.user,
        )

        self.comment = Comment.objects.create(
            article=self.article,
            body="This is a comment",
            name="John Doe",
            email="johndoe@example.com",
        )

    def test_comment_create_view(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.post(
            reverse("comment_add", args={self.article.id}),
            {
                "name": "John Doe",
                "email": "johndoe@example.com",
                "body": "This is a new comment",
                "active": True,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comment.objects.last().body, "This is a new comment")
        # self.assertEqual(Comment.objects.first().body, "This is a new comment")
        # self.assertTrue(self.comment.name == self.user)

    """
    def test_comment_update(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.post(
            reverse("comment_edit", args={self.article.id}),
            {
                "body": "Updated comment",
            },
        )
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(Comment.objects.last().body, "Updated comment")

    def test_comment_delete(self):
        self.client.login(email="johndoe@example.com", name="John Doe", password="secret")
        response = self.client.post(
            reverse("comment_delete", args={self.article.id}),
        )
        self.assertEqual(response.status_code, 302)
        # self.assertNotContains(Message.objects.all().text, "Updated title")
    """

    def test___str__(self):
        assert self.comment.__str__() == "Comment by John Doe on A good title"
        # assert str(self.comment) == self.comment.body


class SitemapTests(TestCase):
    def setUp(self):
        # url = reverse("sitemap")
        url = "/sitemap.xml"
        self.response = self.client.get(url)

    def test_view_url_exists_at_desired_location(self):
        self.assertEqual(self.response.status_code, 200)


class RSSFeedTests(TestCase):
    def setUp(self):
        url = reverse("article_feed")
        self.response = self.client.get(url)

    def test_feed_url_exists_at_desired_location(self):
        self.assertEqual(self.response.status_code, 200)
