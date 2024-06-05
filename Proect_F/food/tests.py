from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Food

class FoodModelTest(TestCase):
    def setUp(self):
        self.food = Food.objects.create(name="Test Food", calorie_amount=100, protein_amount=10.0, carb_amount=20.0, fat_amount=5.0)

    def test_food_creation(self):
        food = Food.objects.get(name="Test Food")
        self.assertEqual(food.calorie_amount, 100)

class FoodAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.food = Food.objects.create(name="Test Food", calorie_amount=100, protein_amount=10.0, carb_amount=20.0, fat_amount=5.0)

    def test_get_foods(self):
        response = self.client.get('/api/foods/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_food(self):
        data = {'name': 'New Food', 'calorie_amount': 200, 'protein_amount': 15.0, 'carb_amount': 30.0, 'fat_amount': 10.0}
        response = self.client.post('/api/foods/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Food.objects.count(), 2)
