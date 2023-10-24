from django.shortcuts import render
from django.views import generic
from .models import Recipe, Rating, Comment, Favorite, Category, CommentLike


# Recipe View: Handles the recipe posts
class RecipeView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status='published').order_by('-all_ratings')
    template_name = 'index.html'

