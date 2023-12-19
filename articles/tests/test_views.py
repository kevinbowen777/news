import pytest
from django.urls import reverse
from pytest_django.asserts import (
    assertContains,
    assertTemplateUsed,
)

from ..models import Article
from ..views import (
    article_create,
    article_delete,
    article_detail,
    article_update,
)

# pytestmark = pytest.mark.django_db


@pytest.mark.django_db
def test_article_create_view(rf, admin_user):
    form_data = {
        "title": "A news article",
        "slug": "",
        "tags": "testingishard, placeholder",
        "status": "PB",
        "body": "This is serious news",
    }
    # Make a request for our new message
    request = rf.post(reverse("article_new"), form_data)
    # Add an authenticated user
    request.user = admin_user
    # Use the request to get the response
    response = article_create(request)
    # Test that the response is valid
    assert response.status_code == 302


@pytest.mark.django_db
def test_article_detail_view(rf, article, admin_user):
    # Get the request
    url = f"{article.publish}/{article.slug}/"
    request = rf.get(url)
    request.user = admin_user
    # Use the request to get the response
    response = article_detail(
        request,
        year=article.publish.year,
        month=article.publish.month,
        day=article.publish.day,
        article=article.slug,
    )
    # Test that the response is valid
    assertContains(response, article.title)


"""
@pytest.mark.django_db
def test_article_list_view(rf, ten_articles, admin_user):
    # Get the request
    request = rf.get(reverse("article_list"))
    request.user = admin_user
    # Use the request to get the response
    response = article_list(request)
    html = response.content.decode("utf-8")
    for i in range(10):
        i += 1
        assert f"A Tiny Test Article {i}" in html
    # Test that the response is valid
    assert response.status_code == 200
    assertContains(response, "Latest News Articles")
    # assert response.content[:].number == 10
    # assert "is_paginated" in response.context
    # assert (response.context("is_paginated") is True)
    # assert len(response.context["article_list"]) == 5
"""


@pytest.mark.django_db
def test_article_delete(rf, article):
    request = rf.post(
        reverse("article_delete", kwargs={"pk": article.id}),
    )
    request.user = article.author
    callable_obj = article_delete
    response = callable_obj(request, pk=article.id)
    assert request.method == "POST"
    assert response.status_code == 302


@pytest.mark.django_db
def test_article_delete_bad_author(rf, article, user):
    request = rf.get(
        reverse("article_delete", kwargs={"pk": article.id}),
    )
    request.user = user
    callable_obj = article_delete
    response = callable_obj(request, pk=article.id)
    assert response.status_code == 200


@pytest.mark.django_db
def test_article_update(rf, article):
    """POST request to message_update updates a message
    and redirects.
    """
    form_data = {
        "title": article.title,
        "status": article.status,
        "tags": "newtag, thistag, thenews",
        "body": "This is the new article body",
    }
    url = reverse("article_update", kwargs={"pk": article.id})
    # Make a request for our updated message
    request = rf.post(url, form_data)
    request.user = article.author
    callable_obj = article_update
    response = callable_obj(request, pk=article.id)

    # Check that the message body has been changed
    article.refresh_from_db()
    text = Article.published.last()
    assert response.status_code == 302
    assert text.author == article.author


@pytest.mark.django_db
def test_article_create(client, user):
    client.login(email=user.email, password="P@s5word")
    response = client.get("/articles/new/")
    assert response.status_code == 200
    assertTemplateUsed(response, "articles/article_new.html")


@pytest.mark.django_db
def test_article_list_pagination(rf, client, ten_articles, user):
    client.login(email=user.email, password=user.password)
    # response = rf.get("articles/?page=2")
    response = client.get("/articles/")
    assert response.status_code == 200
    # assertTemplateUsed(response, "articles/article_list.html")
    # assert response.context["is_paginated"]
    # assertContains(response.content, "is_paginated")
    # assert response.context["is_paginated"] is True
    # assert len(response.context["article_list"]) == 5


@pytest.mark.django_db
def test_comment_add(client, article, user):
    client.login(email=user.email, password="P@s5word")
    # form = "templates/articles/includes/comment_form.html"
    response = client.post(
        reverse("comment_add", kwargs={"article_id": article.id}),
        {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "body": "This is a new comment",
        },
    )

    assert response.status_code, 200


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


@pytest.mark.django_db
def test_sitemap(client, ten_articles):
    response = client.get("/sitemap.xml")
    xml = response.content.decode("utf-8")
    expected_articles = [a for a in ten_articles]
    assert response.status_code == 200
    assert len(expected_articles) == 10
    assert "<lastmod>" in xml


@pytest.mark.django_db
def test_rssfeed(client, ten_articles):
    response = client.get(reverse("article_feed"))
    xml = response.content.decode("utf-8")
    expected_articles = [a for a in ten_articles]
    assert len(expected_articles) == 10
    assert response["Content-Type"] == "application/rss+xml; charset=utf-8"
    assert response.status_code == 200
    assert "<title>news</title>" in xml
