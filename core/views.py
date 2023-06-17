from django.shortcuts import render
from core.models import Recipe
# Create your views here.

def all_recipes(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'all_recipes.html', context)
