from typing import Any
from django.db import models

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.item
    


class Task(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()


class Action(models.Model):
    user = models.ForeignKey(Task, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Task, on_delete=models.CASCADE)