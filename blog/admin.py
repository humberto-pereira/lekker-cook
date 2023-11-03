from django.contrib import admin
from .models import Recipe, Rating, Comment, Category, Carousel
from django_summernote.admin import SummernoteModelAdmin
from .forms import RecipeAdminForm


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_date', 'author')
    list_display = ('title', 'slug', 'status', 'created_date', 'author')
    summernote_fields = ('content')


admin.site.register(Rating)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'recipe', 'content', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'content', 'email')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'image')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('heading', 'caption', 'image')
    search_fields = ('heading', 'caption')
    list_filter = ('heading',)

admin.site.register(Carousel, CarouselAdmin)