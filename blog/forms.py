from django import forms
from .models import Recipe, Category


class RecipeAdminForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.RadioSelect,
        required=True
    )