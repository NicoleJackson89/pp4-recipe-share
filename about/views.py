from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactUsForm


def about_rs(request):
    """
    Renders the most recent information on the about page
    for the website :model:`about.About`.
    """
    if request.method == "POST":
        contact_form = ContactUsForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request,
                             "Message received! We respond within 24 hours.")

    about = About.objects.all().order_by('-updated_on').first()
    contact_form = ContactUsForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
         "contact_form": contact_form},
    )
