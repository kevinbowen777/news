"""
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
