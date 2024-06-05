from django.db import models
from users.models import User
from food.models import Food

class UserFoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

class CalorieRequirement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    calorie_goal = models.IntegerField()

class UserFoodRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
