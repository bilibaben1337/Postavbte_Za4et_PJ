from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from users.models import User
from food.models import Food
from .models import UserFoodLog, CalorieRequirement, UserFoodRecommendation

class LogModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="Test User", age=30, gender="Male", weight=70.0, height=175.0, activity_level="moderate", goal="maintain weight")
        self.food = Food.objects.create(name="Test Food", calorie_amount=100, protein_amount=10.0, carb_amount=20.0, fat_amount=5.0)
        self.log = UserFoodLog.objects.create(user=self.user, food=self.food, date_time="2023-01-01T12:00:00Z")
        self.calorie_requirement = CalorieRequirement.objects.create(user=self.user, calorie_goal=2000)
        self.recommendation = UserFoodRecommendation.objects.create(user=self.user, food=self.food)

    def test_log_creation(self):
        log = UserFoodLog.objects.get(id=self.log.id)
        self.assertEqual(log.food.name, "Test Food")

    def test_calorie_requirement_creation(self):
        calorie_requirement = CalorieRequirement.objects.get(id=self.calorie_requirement.id)
        self.assertEqual(calorie_requirement.calorie_goal, 2000)

    def test_recommendation_creation(self):
        recommendation = UserFoodRecommendation.objects.get(id=self.recommendation.id)
        self.assertEqual(recommendation.food.name, "Test Food")

class LogAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(name="Test User", age=30, gender="Male", weight=70.0, height=175.0, activity_level="moderate", goal="maintain weight")
        self.food = Food.objects.create(name="Test Food", calorie_amount=100, protein_amount=10.0, carb_amount=20.0, fat_amount=5.0)
        self.log = UserFoodLog.objects.create(user=self.user, food=self.food, date_time="2023-01-01T12:00:00Z")
        self.calorie_requirement = CalorieRequirement.objects.create(user=self.user, calorie_goal=2000)
        self.recommendation = UserFoodRecommendation.objects.create(user=self.user, food=self.food)

    def test_get_logs(self):
        response = self.client.get('/api/user-food-logs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_log(self):
        data = {'user': self.user.id, 'food': self.food.id, 'date_time': "2023-01-02T12:00:00Z"}
        response = self.client.post('/api/user-food-logs/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserFoodLog.objects.count(), 2)
