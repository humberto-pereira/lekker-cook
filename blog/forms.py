from django import forms
from .models import Recipe, Category, Comment


class RecipeAdminForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=True
    )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'comment-box',
        'placeholder': 'Write your comment here!',
        'rows': 4,
        'cols': 30,
        })
    )