from django.db import models


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.JSONField(default=list)
    image = models.ImageField(upload_to='images/recipes/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    liked_by = models.ManyToManyField('auth.User', related_name='liked_recipes', blank=True)

    def __str__(self):
        return self.title
    
    def get_like_count(self):
        return self.liked_by.count()
