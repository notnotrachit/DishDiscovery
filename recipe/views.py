from django.shortcuts import render, redirect
from recipe.models import Recipe
from django.http import JsonResponse
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
        recipe = Recipe(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            ingredients=request.POST.get('ingredients'),
            steps=request.POST.getlist('instructions'),
            image=request.FILES.get('image'),
            created_by=request.user
        )
        recipe.save()
        return redirect('recipe_detail', pk=recipe.pk)
    else:
        return render(request, 'new_recipe.html')
    

def toggle_like_recipe(request, pk):
    if request.method != 'POST':
        return redirect('recipe_detail', pk=pk)
    recipe = Recipe.objects.get(pk=pk)
    if request.user in recipe.liked_by.all():
        recipe.liked_by.remove(request.user)
    else:
        recipe.liked_by.add(request.user)
    new_like_status = request.user in recipe.liked_by.all()
    return JsonResponse({'success': True, 'new_like_count': recipe.get_like_count(), 'new_like_status': new_like_status})


def profile(request):
    recipes = Recipe.objects.filter(created_by=request.user)
    context = {
        'recipes': recipes
    }
    return render(request, 'profile.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    original_image = recipe.image
    if request.method == 'POST':
        recipe.title = request.POST.get('title')
        recipe.description = request.POST.get('description')
        recipe.ingredients = request.POST.get('ingredients')
        recipe.steps = request.POST.getlist('instructions')
        if request.FILES.get('image'):
            recipe.image = request.FILES.get('image')
        else:
            recipe.image = original_image
        recipe.save()
        return redirect('recipe_detail', pk=recipe.pk)
    else:
        context = {
            'recipe': recipe
        }
        return render(request, 'edit_recipe.html', context)

