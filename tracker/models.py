from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name
