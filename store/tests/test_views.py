from django.http import request
from store.views import all_products
from unittest import skip

from django.contrib.auth.models import User
from django.http.request import HttpRequest
from django.test import Client, TestCase, RequestFactory
from django.urls.base import reverse
from store.models import Category, Product


class TestViewResponse(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        User.objects.create(username="admin")
        Category.objects.create(name="django", slug="django")
        Product.objects.create(
            category_id=1,
            title="django beginners",
            created_by_id=1,
            slug="django-beginners",
            price="20.00",
            image="django",
        )

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test Product response status
        """
        response = self.client.get(reverse("product_detail", args=["django-beginners"]))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test category response status
        """
        response = self.client.get(reverse("category_list", args=["django"]))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        response = all_products(HttpRequest())
        html = response.content.decode("utf8")
        self.assertIn("<title>Home</title>", html)
        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get("/item/django-beginners")
        response = all_products(request)
        html = response.content.decode("utf8")
        self.assertIn("<title>Home</title>", html)
        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code, 200)
