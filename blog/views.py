from django.shortcuts import render
from .models import Category, Recipe


def category_list(request):
    categories = Category.objects.all().prefetch_related('recipe_set')
    
    category_data = []
    for category in categories:
        recipes = Recipe.objects.filter(category=category)
        category_data.append({
            'category': category,
            'recipes_count': recipes.count(),
            'recipes': recipes[:5],  # Display up to 5 recipes from each category
        })
    
    return render(request, 'index.html', {'categories': category_data})


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})