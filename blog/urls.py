from django.urls import path
from . import views


urlpatterns = [
    path('', views.category_list, name='home'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),

]