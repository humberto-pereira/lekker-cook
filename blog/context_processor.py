from .models import Category

def category_links(request):
    """
    Returns a dictionary of all categories to be used in the base.html template.
    """
    categories = Category.objects.all()
    return {'categories': categories}