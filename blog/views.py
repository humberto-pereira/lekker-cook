from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Recipe
from django.db.models import Avg
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.urls import reverse


def category_list(request):
    categories = Category.objects.all().prefetch_related('recipes')
    
    category_data = []
    for category in categories:
        recipes = Recipe.objects.filter(category=category)
        category_data.append({
            'category': category,
            'recipes_count': recipes.count(),
            'recipes': recipes[:5],  # Display up to 5 recipes from each category
        })
    
    return render(request, 'index.html', {'categories': category_data})


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    comments = recipe.comments.filter(approved=True)  # only approved comments
    return render(request, 'recipe_detail.html', {'recipe': recipe, 'comments': comments})


def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    recipes = Recipe.objects.filter(category=category).annotate(annotated_average_rating=Avg('ratings__stars')).order_by('-annotated_average_rating', '-created_date')
    return render(request, 'category_detail.html',
                  {'category': category, 'recipes': recipes})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # save the user
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'You have been logged out.')
        return redirect('home')
    else:
        #render the logout page if method is GET
        return render(request, 'registration/logout.html')