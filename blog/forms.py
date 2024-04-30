from .models import Comment, Recipe
from django import forms
# from crispy_forms.helper import FormHelper


class CommentForm(forms.ModelForm):
    """
    Form to allow customisation on the comment form
    """
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': '',}
        

class RecipePostForm(forms.ModelForm):
    """
    Form to allow customisation on create a recipe
    """
    class Meta:
        model = Recipe
        fields = ('title', 'excerpt', 'feat_img', 'prep_time', 
                  'cook_time', 'servings', 'ingredients', 'instructions', 
                  'notes')