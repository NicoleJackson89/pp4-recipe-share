from django.contrib import admin
from .models import MyProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(MyProfile)
class MyProfileAdmin(SummernoteModelAdmin):
    """
    Adds text editing of My profile in admin panel
    """
    fullname = ('author',)
    email = ('email',)
    about_me = ('status',)
    summernote_fields = ('about_me',)