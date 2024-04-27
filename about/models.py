from django.db import models


class About(models.Model):
    """
    Stores a single about me text
    """
    title = models.CharField(max_length=200)
    # feat_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    body = models.TextField()

    def __str__(self):
        return self.title
    

# WILL NEED TO GO TO contact us page
class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contact_nr = models.CharField(max_length=200)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact request received from {self.name}"