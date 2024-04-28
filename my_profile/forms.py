from django import forms
from django.contrib.auth.models import User
from .models import MyProfile

# class ProfileUpdateForm(forms.ModelForm):
#     """
#     Customisation form for my profile
#     """
#     class Meta:
#         model = MyProfile
#         fields = ('username', 'feat_img', 'fullname', 'email', 'about_me')