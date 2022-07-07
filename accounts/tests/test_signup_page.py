from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from ..views import SignupPageView


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="kevin",
            email="kevin@example.com",
            password="T3stP@ss123!",
        )
        self.assertEqual(user.username, "kevin")
        self.assertEqual(user.email, "kevin@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNotNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(username="", email="", password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        super_user = User.objects.create_superuser(
            username="superadmin",
            email="superadmin@example.com",
            password="t3stP@ss123!",
        )
        self.assertEqual(super_user.username, "superadmin")
        self.assertEqual(super_user.email, "superadmin@example.com")
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
        try:
            self.assertIsNotNone(super_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username="",
                email="super@user.com",
                password="foo",
                is_superuser=False,
            )

    def test_get_absolute_url(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="kevin",
            email="kevin@example.com",
            password="T3stP@ss123!",
        )
        self.assertEqual(user.get_absolute_url(), "/accounts/kevin/")


class SignupPageTests(TestCase):

    username = "newuser"
    email = "newuser@example.com"

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "This does not belong here.")

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(  # noqa:F841
            self.username, self.email
        )
        self.assertContains(self.response, "csrfmiddlewaretoken")
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(
            get_user_model().objects.all()[0].username, self.username
        )
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)

    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__,
        )
