from django.contrib import admin
from .models import Recipe, Rating
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')


admin.site.register(Rating)
