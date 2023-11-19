from .models import Category
"""
A custom context processor to make the categories available to all templates.

"""
def category_processor(request):
    return {'categories': Category.objects.all()}