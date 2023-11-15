from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.category_list, name='home'),
    path('recipe/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    #  Login register and logout views
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/', include('allauth.urls')),
    path('edit_comment/<int:pk>/', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:pk>/', views.delete_comment, name='delete_comment'),
    path('like_comment/<int:comment_id>/', views.like_comment, name='like_comment'),
    path('recipe/<slug:slug>/rate/', views.rate_recipe, name='rate_recipe'),
    path('favorites/', views.favorites, name='favorites'),
    path('add_favorite/<int:recipe_id>/', views.add_to_favorite, name='add_to_favorite'),
    path('remove_from_favorite/<int:favorite_id>/', views.remove_from_favorite, name='remove_from_favorite'),
    path('toggle_favorite/<int:recipe_id>/', views.toggle_favorite, name='toggle_favorite'),
]
