from urllib import response
from django.test import Client, TestCase
from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse
from django.contrib.auth.models import User

from adminPanel.views import addBrand, addCategory, adminProducts, productEdit
from product.models import Brand, Category, Products


# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_case_products_url(self):
        url=reverse('adminproducts')

        self.assertEqual(resolve(url).func,adminProducts)

    def test_case_category_url(self):
        url=reverse('categoryAdd')

        self.assertEqual(resolve(url).func,addCategory)

    def test_case_brand_url(self):
        url=reverse('brandAdd')

        self.assertEqual(resolve(url).func,addBrand)

    def test_case_prodedit_url(self):
        url=reverse('prodEdit',args=[2])

        self.assertEqual(resolve(url).func,productEdit)

class TestViews(TestCase):
    def test_case_prodAdd_views(self):
        user=User.objects.create(username="newGuy")
        user.set_password('123456')
        user.save()

        client=Client()


        logged_in=client.login(username='newGuy',password="123456")
    

        url=reverse('prodAdd')

        response=client.post(url,{
            'name':'test name',
            'price' : 0,
            'brand':"Thakali",
            'category' :"Oil",
            'description':'test desc',
            'search_tags':'test tag',
            'available': True,
            'image':'test image',
        })
    
        self.assertEquals(response.status_code,200)

    def test_case_deleteProdviews(self):
        user=User.objects.create(username="newGuy")
        user.set_password('123456')
        user.save()

        client=Client()
        print(client)

        logged_in=client.login(username='newGuy',password="123456")
        print(logged_in)
        

        newlyCreated=Products.objects.create(
            name='test name',
            price = 0,
            brand=Brand.objects.create(name="Pampers"),
            category =Category.objects.create(name="BabyCare"),
            description='test desc',
            search_tags='test tag',
            available= True,
            image='test image',
        )
        print(newlyCreated.id)
        url=reverse('prodDelete',args=[newlyCreated.id])
        print(url)

        response =client.delete(url)
        
    
        self.assertEquals(response.status_code,302)
