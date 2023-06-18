from django.db import models


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.JSONField(default=list)
    image = models.ImageField(upload_to='images/recipes/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
