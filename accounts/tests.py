from urllib import request, response
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class SignUpPageTests(TestCase):
    def setUp(self) -> None:
        self.email:'newadmin@gmail.com'
        self.first_name: 'admin'
        self.last_name: 'prajapati'
        self.username: 'admin2'
        self.password1: 'admin2'
        self.password2: 'admin2'

    def test_signup_page_url(self):
        response = self.client.get('/accounts/register')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register.html')

    def test_signup_page_view_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register.html')

    def test_signup_form(self):
        response = self.client.post(reverse('register'), form={
            'first_name': self.first_name,
            'username': self.username,
            'email': self.email,
            'last_name': self.last_name,
            'password1': self.password1,
            'password2': self.password2
        })
        self.assertEqual(response.status_code, 200)

        users = User.objects.all()
        self.assertEqual(users.count(), 1)