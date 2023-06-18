from django.shortcuts import render, redirect
from recipe.models import Recipe
# Create your views here.

def all_recipes(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'all_recipes.html', context)


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        'recipe': recipe
    }
    return render(request, 'recipe_detail.html', context)


def new_recipe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')
        image = request.FILES.get('image')
        recipe = Recipe(name=name, description=description, ingredients=ingredients, instructions=instructions, image=image)
        recipe.save()
        return render(request, 'new_recipe.html')
    else:
        return render(request, 'new_recipe.html')
    
