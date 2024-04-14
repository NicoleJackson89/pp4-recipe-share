from django.db import models
from django.contrib.auth.models import User


class MyProfile(models.Model):
    """
    Stores a users profile, related to :model:`auth.User`.
    """
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    # feat_img = CloudinaryField('image', default='placeholder')
    fullname = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=False)
    about_me = models.TextField(blank=True)
    
    
    class Meta:
        ordering = ["username", "email"]

    def __str__(self):
        return f"User: {self.username} | Email: {self.email}"

