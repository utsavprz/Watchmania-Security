from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse

from home.views import index
from product.views import detail

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_index_url(self):
        url=reverse('index')
        self.assertEqual(resolve(url).func,index)

        

class TestDetailsUrls(SimpleTestCase):
    def test_case_detail_url(self):
        url=reverse('detail',args=[1])
        self.assertEqual(resolve(url).func,detail)