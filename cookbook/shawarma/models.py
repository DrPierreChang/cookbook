from django.db import models


class Shawarma(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField('Ingredient', blank=False)
    description = models.TextField()



class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
