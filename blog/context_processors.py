from .models import Category
"""
A custom context processor to make the categories available to all templates.

"""
def category_processor(request):
    """
    Returns all categories to be available to all templates.
    """
    return {'categories': Category.objects.all()}