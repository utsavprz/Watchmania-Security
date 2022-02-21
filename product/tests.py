from django.test import Client, SimpleTestCase, TestCase
from django.urls import resolve, reverse
from django.contrib.auth.models import User


from product.views import detail
# Create your tests here.

class TestDetailsUrls(TestCase):
    def test_case_detail_url(self):
        url=reverse('detail',args=[51])
        self.assertEqual(resolve(url).func,detail)


        
