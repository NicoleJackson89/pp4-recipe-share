from django.shortcuts import render
from .models import About
from .forms import ContactUsForm


def about_rs(request):
    """
    Renders the most recent information on the about page
    for the website :model:`about.About`.
    """

    about = About.objects.all().order_by('-updated_on').first()
    contact_form = ContactUsForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
         "contact_form": contact_form},
    )