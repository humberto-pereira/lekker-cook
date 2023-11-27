from django.contrib import admin
from .models import Recipe, Rating, Comment, Category, Carousel
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Recipe model with summernote integration. Define
    the list display, search fields, list filter, and prepopulated fields.
    """

    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_date', 'author')
    list_display = ('title', 'category', 'slug', 'status',
                    'created_date', 'author')
    summernote_fields = ('content')


# Simple registration of the Rating model.
admin.site.register(Rating)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin interface for the Comment model. Define the list display,
    search fields, list filter, and custom actions such as comment approval.
    """
    list_display = ('user_name', 'recipe', 'content', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'content', 'email')
    actions = ['approve_comments']

    def user_name(self, obj):
        """
        Display the name of the user who created the comment.
        """
        return obj.user.username

    def approve_comments(self, request, queryset):
        """
        Admin action to approve comments.
        """
        queryset.update(approved=True)


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for the Category model. Includes configuration for the
    list display and prepopulated slug field."""
    list_display = ('name', 'slug', 'description', 'image')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class CarouselAdmin(admin.ModelAdmin):
    """
    Admin interface for the Carousel model. Includes configuration for the
    list display, search fields, and list filter."""
    list_display = ('heading', 'caption', 'image')
    search_fields = ('heading', 'caption')
    list_filter = ('heading',)
    

admin.site.register(Carousel, CarouselAdmin)