from django.test import TestCase
from django.urls import resolve, reverse
from .views import signup_view
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your tests here.

class SingUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_singup_status_code(self):
        self.assertEquals(self.response.status_code, 200)
    
    def test_signup_url_resolvers_signup_view(self):
        view = resolve('/signup/')
        self.assertEquals(view.func, signup_view)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserCreationForm)

class SuccessfulSignupTests(TestCase):
    def  setUp(self):
        url = reverse('signup')
        data = {
           'username': 'john',
           'email': 'jd@gmail.com',
           'password1': '12345679Kl',
           'password2': '12345679Kl',
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')
    
    def test_redirection(self):
        
          #successful signup shld redirect to home page
        self.assertRedirects(self.response, self.home_url)
    
    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        '''
        create a new request and shld have response of user to its context
        after a successful sign up
        '''
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


 