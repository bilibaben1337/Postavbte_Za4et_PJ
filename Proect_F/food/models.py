from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    calorie_amount = models.IntegerField()
    protein_amount = models.FloatField()
    carb_amount = models.FloatField()
    fat_amount = models.FloatField()
