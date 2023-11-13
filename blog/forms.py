from django import forms
from .models import Recipe, Category, Comment, Rating


class RecipeAdminForm(forms.ModelForm):
    """
    A ModelForm subclass to handle the creation and updating 
    of Recipe objects within the Django interface.
    """
    class Meta:
        model = Recipe
        fields = '__all__'

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=True
    )

class CommentForm(forms.ModelForm):
    """
    A Modelform subclass for creating Comment objects. It exposes only the 'content' field.
    field, which uses a custon Textarea widget with specific attributes.
    """
    class Meta:
        model = Comment
        fields = ('content',)
        content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'comment-form-textarea',
        'placeholder': 'Write your comment here!',
        'rows': 5,
        'cols': 30,
        })
    )
        

class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ('stars',)