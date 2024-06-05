from django.test import TestCase
from django.contrib.auth.models import User as AuthUser
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, UserActivity, UserGoal

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="Test User", age=30, gender="Male", weight=70.0, height=175.0, activity_level="moderate", goal="maintain weight")

    def test_user_creation(self):
        user = User.objects.get(name="Test User")
        self.assertEqual(user.age, 30)

class UserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = AuthUser.objects.create_user(username='testuser', password='testpass')

    def test_register_user(self):
        url = '/api/register/'
        data = {'username': 'newuser', 'password': 'newpass', 'email': 'newuser@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        url = '/api/login/'
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_users(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
