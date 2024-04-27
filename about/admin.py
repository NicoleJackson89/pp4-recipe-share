from django.contrib import admin
from .models import About, ContactUs
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Adds text editing of the body in admin panel
    """
    summernote_fields = ('body',)


# WILL NEED TO GO TO contact us page
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)