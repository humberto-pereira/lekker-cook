from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.category_list, name='home'),
    path('recipe/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    #  Login register and logout views
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
