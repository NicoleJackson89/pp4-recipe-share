from .models import Comment, Recipe
from django import forms
from crispy_forms.helper import FormHelper
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    """
    Form to allow customization on the comment form
    """
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': '',}
        

class RecipePostForm(forms.ModelForm):
    """
    Form to allow customization on create a recipe
    """
    class Meta:
        model = Recipe
        fields = ('title', 'excerpt', 'feat_img', 'prep_time', 
                  'cook_time', 'servings', 'ingredients', 'instructions', 
                  'notes')
        widgets = {
            'ingredients': SummernoteWidget(attrs={"class": "form-control"}),
            'instructions': SummernoteWidget(attrs={"class": "form-control"}),
            }