from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Recipe, Carousel, Comment, Rating, Favorite
from .forms import CommentForm, RatingForm
from django.db.models import Avg
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_POST


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
            'recipes': recipes[:5],  # Display up to 5 recipes from each
                                     # category
        })
    carousel_items = Carousel.objects.all()

    return render(request, 'index.html', {
        'categories': category_data,
        'carousel_items': carousel_items,
        'hide_categories_menu': True
        })


@login_required
def recipe_detail(request, slug):
    """
    Display a single recipe detail page with approved comments
    and rating submission.

    param request: HttpRequest object
    param slug: Thej slug of the recipe to retrieve
    :return: HttpResponse object with the rendered recipe_detail.html template
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.user.is_authenticated:
        favorited_recipe_ids = set(Favorite.objects.filter(
            user=request.user).values_list('recipe_id', flat=True))
    else:
        favorited_recipe_ids = set()
    all_comments = recipe.comments.all()  # Get all comments for the recipe
    new_comment = None
    # Initialize the form for both GET and POST requests
    comment_form = CommentForm()
    # Initialize the rating form for both GET and POST requests
    rating_form = RatingForm()

    if request.method == 'POST':
        # check if it's a comment submission
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

    elif 'submit-rating' in request.POST:
        # check if it's a rating submission
        rating_form = RatingForm(data=request.POST)
        if rating_form.is_valid():
            # check if the user has already rated the recipe
            rating_form = RatingForm(data=request.POST)
            rating, created = Rating.objects.get_or_create(
                recipe=recipe,
                user=request.user,
                defaults={'stars': rating_form.cleaned_data['stars']}
            )
            if not created:
                # Rating already exists, update the existing stars
                rating.stars = rating_form.cleaned_data['stars']
                rating.save()

            return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
        # get the user existing rating if it exists
    user_rating = None
    if request.user.is_authenticated:
        # check if the user has already rated the recipe
        user_rating = Rating.objects.filter(recipe=recipe,
                                            user=request.user).first()

    return render(request, 'recipe_detail.html', {
        'recipe': recipe,
        'comments': all_comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'rating_form': rating_form,
        'user_rating': user_rating,
        'favorited_recipe_ids': favorited_recipe_ids,
    })


def category_detail(request, slug):
    """
    Display the detail view of a category and its associated
    recipes ordered by rating.

    param request: HttpRequest object
    param slug: The slug of the category to retrieve
    return: HttpResponse object with the rendered
    category_detail.html template
    """
    category = get_object_or_404(Category, slug=slug)
    recipes = Recipe.objects.filter(category=category).annotate(
        annotated_average_rating=Avg('ratings__stars'
                                     )).order_by('-annotated_average_rating',
                                                 '-created_date')
    if request.user.is_authenticated:
        favorited_recipe_ids = set(Favorite.objects.filter(user=request.user)
                                   .values_list('recipe_id', flat=True))
    else:
        favorited_recipe_ids = set()
    return render(request, 'category_detail.html',
                  {'category': category,
                   'recipes': recipes,
                   'favorited_recipe_ids': favorited_recipe_ids,
                   })


def signup(request):
    """
    Handle user registration

    param request: HttpRequest object
    return: HttpResponse object with the rendered signup.html template or
    redirect to the home page if the user is logged in
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
    return: HttpResponse object with the rendered logout.html template or
    redirect to the home page if the user is logged out
    """
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'You have been logged out.')
        return redirect('home')
    else:
        # render the logout page if method is GET
        return render(request, 'registration/logout.html')


@login_required
def edit_comment(request, pk):
    """
    Alllow users to edit their own comments. On POSt, updates and marks
    the comment as not approved.
    redirecting to the recipe detail page.
    param request (HttpRequest): The request object containing the request data
    pk (int): Primary key of the comment to be edited

    Returns: HttpResponse edit comment form or a redirect to the
    recipe detail page
    """
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
    """
    Allow authenticated users to delete their own comments. On POST,
    deletes the comment and redirects to the recipe detail page. on GET,
    displays a confirmation page.

    param request (HttpRequest): The request object containing the request data
    pk (int): Primary key of the comment to be deleted

    returns: HttpResponse confirmation page or a redirect to the
    recipe detail page
    """
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    recipe_slug = comment.recipe.slug
    if request.method == 'POST':
        comment.delete()
        messages.success(request, ' your comment has been deleted.')
        return redirect('recipe_detail', slug=recipe_slug)
    return render(request, 'confirm_delete.html', {'comment': comment})


@login_required
def like_comment(request, comment_id):
    """
    Allow authenticated users to like comments. On POST, adds or
    removes the user from the comment's likes and
    returns the updated like count.

    param request (HttpRequest): The request object containing the request data
    comment_id (int): Primary key of the comment to be liked

    returns: JsonResponse containing the updated like count
    """
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
    return JsonResponse({'likes_count': comment.like_count})


@login_required
@require_POST
def rate_recipe(request, slug):
    """
    Allow authenticated users to rate recipes. On POST, creates
    or updates the rating and returns the updated average rating.

    param request (HttpRequest): The request object containing
    the request data
    slug (str): The slug of the recipe to be rated

    returns: JsonResponse containing the updated average rating
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    form = RatingForm(request.POST)
    if form.is_valid():
        # This gets the existing rating if it exists, or none otherwise
        rating, created = Rating.objects.get_or_create(
            user=request.user,
            recipe=recipe,
            defaults={'stars': form.cleaned_data['stars']}
        )
        if not created:
            # Rating already exists, so update the stars and save
            rating.stars = form.cleaned_data['stars']
            rating.save()
            message = 'Your rating has been updated.'
        else:
            message = 'Your rating has been submitted.'

        # Refresh the recipe to update average rating
        recipe.refresh_from_db()
        return JsonResponse({'success': True, 'average_rating':
                             recipe.average_rating, 'message': message})
    else:
        # If the form is not valid, send back the error messages
        return JsonResponse({'success': False, 'errors':
                             form.errors}, status=400)


@login_required
def favorites(request):
    """
    Display a list of the user's favorite recipes.

    param request: HttpRequest object

    return: HttpResponse object with the rendered favorites.html template
    """
    user_favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites.html', {'favorites': user_favorites})


@login_required
def add_to_favorite(request, recipe_id):
    """
    Add a recipe to the user's favorites.

    param request: HttpRequest object
    param recipe_id: The id of the recipe to add to favorites

    return: HttpResponse redirect to the previous page or the home page
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user,
                                                       recipe=recipe)
    if created:
        messages.success(request, 'Recipe added to favorites.')
    else:
        messages.info(request, 'Recipe already in favorites.')
        # redirect to the same page
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def remove_from_favorite(request, favorite_id):
    """
    Remove a recipe from the user's favorites.

    param request: HttpRequest object
    param favorite_id: The id of the favorite to be removed

    return: HttpResponse redirect to the previous page or the home page
    """
    favorite = get_object_or_404(Favorite, id=favorite_id, user=request.user)
    favorite.delete()
    messages.success(request, 'Recipe removed from favorites.')
    # redirect to the same page
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def toggle_favorite(request, recipe_id):
    """
    Toggle the favorite status of a recipe. If the recipe is already a
    favorite, remove it. If it is not a favorite, add it.

    param request: HttpRequest object
    param recipe_id: The id of the recipe to toggle

    return: HttpResponse redirect to the previous page or the home page
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user,
                                                       recipe=recipe)
    if created:
        messages.success(request, 'Recipe added to favorites.')
    else:
        favorite.delete()
        messages.info(request, 'Recipe removed from favorites.')

    return redirect(request.META.get('HTTP_REFERER', 'home'))
