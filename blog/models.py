from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


SERVINGS = [tuple([x, x]) for x in range(1, 13)]
STATUS = ((0, "Draft"), (1, "Published"))
LIKE_OPTIONS = (('Like', 'Like'), ('Unlike', 'Unlike'))


class Recipe(models.Model):
    """
    Stores a Recipe post entered by a user related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    excerpt = models.TextField(blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts"
    )
    feat_img = CloudinaryField('image', default='placeholder')
    prep_time = models.CharField(max_length=100)
    cook_time = models.CharField(max_length=100)
    servings = models.IntegerField(choices=SERVINGS)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField()
    notes = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, blank=True, related_name='recipe_likes',
    )

    class Meta:
        ordering = ["-created_on", "author"]

    def __str__(self):
        return f"Recipe name: {self.title} | Recipe added by: {self.author}"

    def likes_count(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Stores a comment entered by a user related to :model:`auth.User`
    and :model:`blog.Recipe`.
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment: {self.body} | Comment left by: {self.author}"


class RecipeLikes(models.Model):
    """
    Stores a like entry related to :model:`auth.User`
    and :model:`blog.Recipe`.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_likes = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_OPTIONS, default='Like',
                             max_length=10)

    def __str__(self):
        return str(self.post_likes)
