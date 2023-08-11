from ast import arg
from django.test import Client, SimpleTestCase, TestCase
from django.urls import resolve, reverse
from django.contrib.auth.models import User

from home.views import index
from product.views import detail

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_index_url(self):
        url=reverse('index')
        print(url)
        self.assertEqual(resolve(url).func,index)


