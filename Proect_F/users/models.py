from django.db import models

class User(models.Model):
    LOW = 'low'
    MODERATE = 'moderate'
    HIGH = 'high'
    ACTIVITY_LEVEL_CHOICES = [
        (LOW, 'Low'),
        (MODERATE, 'Moderate'),
        (HIGH, 'High'),
    ]
    
    LOSE_WEIGHT = 'lose weight'
    MAINTAIN_WEIGHT = 'maintain weight'
    GAIN_WEIGHT = 'gain weight'
    GOAL_CHOICES = [
        (LOSE_WEIGHT, 'Lose Weight'),
        (MAINTAIN_WEIGHT, 'Maintain Weight'),
        (GAIN_WEIGHT, 'Gain Weight'),
    ]
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    weight = models.FloatField()
    height = models.FloatField()
    activity_level = models.CharField(max_length=10, choices=ACTIVITY_LEVEL_CHOICES)
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES)

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_level = models.CharField(max_length=10, choices=User.ACTIVITY_LEVEL_CHOICES)

class UserGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=20, choices=User.GOAL_CHOICES)
