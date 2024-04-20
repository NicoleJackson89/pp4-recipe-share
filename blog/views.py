from django.shortcuts import render
from django.views import generic
from .models import Recipe


class RecipeList(generic.ListView):
    # queryset = Post.objects.filter(status=1)
    queryset = Recipe.objects.all()
    template_name = "blog/index.html"
    paginate_by = 9