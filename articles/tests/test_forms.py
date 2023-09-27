import pytest
from django.urls import reverse

from ..views import (
    article_create,
    article_update,
)


@pytest.mark.django_db
def test_article_form_valid_on_create_view(rf, admin_user):
    form_data = {
        "title": "A new late night test",
        "body": "This is the body of the form test.",
        "tags": "test, django, article, news",
    }

    request = rf.post(reverse("article_new"), form_data)
    request.user = admin_user

    response = article_create(request)
    assert response.status_code == 200
    assert True


@pytest.mark.django_db
def test_article_form_valid_on_update_view(rf, article, admin_user):
    form_data = {
        "title": "A new late night test",
        "body": "This is the body of the form test.",
        "tags": "newtag",
    }

    url = reverse("article_update", kwargs={"pk": article.id})
    # Make a request for our new message
    request = rf.post(url, form_data)
    request.user = admin_user

    response = article_update(request, pk=article.id)
    assert response.status_code == 200
    assert True
