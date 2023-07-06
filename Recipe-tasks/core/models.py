from django.db import models

# Create your models here.

class Recipe(models.Model):
  tribe = models.CharField(max_length=50)
  recipeType = models.CharField(max_length=200)
  ingredients = models.TextField(null=True, blank=True)
  ingredientsQty = models.TextField(null=True, blank=True)
  desc = models.TextField()

  def __str__(self):
    return self.tribe