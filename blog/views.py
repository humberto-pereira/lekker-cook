from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Recipe, Carousel, Comment
from .forms import CommentForm
from django.db.models import Avg
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .forms import CommentForm



def category_list(request):
    """
    Display the list of categories with a count of recipes in each category.

    param request: HttpRequest object
    return: HttpResponse object with the rendered category_list.html template

    """
    categories = Category.objects.all().prefetch_related('recipes')
    
    category_data = []
    for category in categories:
        recipes = Recipe.objects.filter(category=category)
        category_data.append({
            'category': category,
            'recipes_count': recipes.count(),
            'recipes': recipes[:5],  # Display up to 5 recipes from each category
        })
    carousel_items = Carousel.objects.all()

    return render(request, 'index.html', {'categories': category_data, 'carousel_items': carousel_items})

@login_required
def recipe_detail(request, slug):
    """
    Display a single recipe detail page with approved comments.

    param request: HttpRequest object
    param slug: Thej slug of the recipe to retrieve
    :return: HttpResponse object with the rendered recipe_detail.html template
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    all_comments = recipe.comments.all()  # Get all comments for the recipe
    new_comment = None
    # Initialize the form for both GET and POST requests
    comment_form = CommentForm()
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the logged in user to the comment
            new_comment.user = request.user
            # Assign the current recipe to the comment
            new_comment.recipe = recipe
            # Save the comment to the database
            new_comment.save()
            return HttpResponseRedirect(recipe.get_absolute_url())
            
    return render(request, 'recipe_detail.html', {
        'recipe': recipe, 
        'comments': all_comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    })


def index(request):
    """
    The main page view that displays all the categories.

    param request: HttpRequest object
    return: HttpResponse object with the rendered index.html template
    """
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def category_detail(request, slug):
    """
    Display the detail view of a category and its associated recipes ordered by rating.

    param request: HttpRequest object
    param slug: The slug of the category to retrieve
    return: HttpResponse object with the rendered category_detail.html template
    """
    category = get_object_or_404(Category, slug=slug)
    recipes = Recipe.objects.filter(category=category).annotate(annotated_average_rating=Avg('ratings__stars')).order_by('-annotated_average_rating', '-created_date')
    return render(request, 'category_detail.html',
                  {'category': category, 'recipes': recipes})

def signup(request):
    """
    Handle user registration

    param request: HttpRequest object
    return: HttpResponse object with the rendered signup.html template or redirect to the home page if the user is logged in
    """
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
    """
    Log out the user and redirect to the home page.

    param request: HttpRequest object
    return: HttpResponse object with the rendered logout.html template or redirect to the home page if the user is logged out
    """
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'You have been logged out.')
        return redirect('home')
    else:
        #render the logout page if method is GET
        return render(request, 'registration/logout.html')
    
@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)   
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            edited_comment = form.save(commit=False)
            # set approved to False to mark comment as not approved
            edited_comment.approved = False
            edited_comment.save()
            messages.info(request, 'Your comment is awiting approval.')
            return redirect('recipe_detail', slug=comment.recipe.slug)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit_comment.html', {'form': form}) 

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    recipe_slug = comment.recipe.slug
    if request.method == 'POST':
        comment.delete()
        messages.success(request, ' your comment has been deleted.')
        return redirect('recipe_detail', slug=recipe_slug)
    return render(request, 'confirm_delete.html', {'comment': comment})

@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
    return JsonResponse({'likes_count': comment.like_count})


