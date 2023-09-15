import pytest
from django.test import RequestFactory
from django.urls import reverse

from ..views import (
    article_create,
)

factory = RequestFactory()


@pytest.mark.django_db
def test_article_form_valid_on_create_view(admin_user):
    form_data = {
        "title": "A new late night test",
        "body": "This is the body of the form test.",
    }

    request = factory.post(reverse("article_new"), form_data)
    request.user = admin_user

    response = article_create(request)
    assert response.status_code == 200
    assert True


"""
@pytest.mark.django_db
def test_message_form_valid_on_update_view(rf, message, admin_user):
    form_data = {
        "title": "A new late night test",
        "body": "This is the body of the form test.",
    }

    url = reverse("article_update", kwargs={"pk": message.id})
    # Make a request for our new message
    request = rf.post(url, form_data)
    request.user = admin_user

    response = article_update(request, pk=message.id)
    assert response.status_code == 200
    assert True


from django.test import SimpleTestCase
from django.urls import reverse


class CommentFormTests(SimpleTestCase):
    def setUp(self):
        url = reverse("comment_new")
        self.response = self.client.get(url)
        self.form_data = {
            "from_email": "joe@example.com",
            "subject": "Test Email",
            "message": "This is a test email",
        }

    def test_comment_page_form_is_valid(self):
        response = self.client.post(
            "/comment/",
            data={
                "comment": "This is a test email",
            },
        )
        self.assertEqual(response.status_code, 302)
"""
