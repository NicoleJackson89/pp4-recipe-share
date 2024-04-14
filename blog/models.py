from django.db import models
from django.contrib.auth.models import User

SERVINGS = [tuple([x,x]) for x in range(1,7)]
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Recipe(models.Model):
    """
    Stores a single Recipe post entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    excerpt = models.TextField(blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts"
    )
    # feat_img = CloudinaryField('image', default='placeholder')
    prep_time = models.CharField(max_length=100)
    cook_time = models.CharField(max_length=100)
    servings = models.IntegerField(choices=SERVINGS)
    ingredients = models.TextField(blank=True)
    instruction = models.TextField()
    notes = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    
    
    
