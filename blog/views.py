from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from .models import Recipe, Comment, RecipeLikes, User
from .forms import CommentForm, RecipePostForm


class RecipeList(generic.ListView):
    """
    Returns all published recipes in :model:`blog.Recipe`
    and displays them in a page of 9 posts per page. 
    """
    queryset = Recipe.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 9
    
    
def recipe_detail(request, slug):
    """
    Displays an individual recipe post :model:`blog.Recipe`.
    **Context**

    ``recipe``
        An instance of :model:`blog.Recipe`.
    ``comments``
        All approved comments related to the recipe post.
    ``total_comments``
        A total of approved comments related to the recipe post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`

    **Template:**

    :template:`blog/recipe_detail.html`
    """
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")
    total_comments = recipe.comments.count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.success(request, 'Comment was posted successfully!')
            
    comment_form = CommentForm()

    return render(
        request,
        "blog/recipe_detail.html",
        {
            "recipe": recipe,
            "comments": comments,
            "total_comments": total_comments,
            "comment_form": comment_form,
        }
    )
    
    
class RecipeLikes(View):
    """
    The view to create likes on Recipe posts
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Recipe, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
    

class RecipeCreate(SuccessMessageMixin, CreateView):
    """
    View for creating a recipe post
    """
    model = Recipe
    form_class = RecipePostForm
    template_name = "recipe_create.html"
    success_url = reverse_lazy("home")
    success_message = "Your recipe has been posted!"

    def form_valid(self, form):
        """
        Adds the logged in user as author of the recipe post
        """
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
    
    
class RecipeUpdate(SuccessMessageMixin, UpdateView):
    """
    View for updating an existing recipe post
    """
    model = Recipe
    form_class = RecipePostForm
    template_name = "recipe_update.html"
    success_message = "Your recipe has been updated successfully!"

    def get_queryset(self):
        """
        Queryset to ensure that the author of the recipe can update it.
        """
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def get_success_url(self):
        """
        Redirects back to the home page after updating successfully
        """
        return reverse('recipe_detail', kwargs={"slug": self.object.slug})
    

class RecipeDelete(SuccessMessageMixin, DeleteView):
    """
    View for deleting an existing recipe post
    """
    model = Recipe
    template_name = "recipe_delete.html"
    success_url = reverse_lazy("home")
    success_message = "Your recipe has been deleted!"

    def test_func(self):
        """
        Ensures the user is the recipe author
        """
        post = self.get_object()
        return self.request.user == post.author
    
    
def comment_edit(request, slug, comment_id):
    """
    The view to edit comments on Recipe posts 
    """
    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment has been successfully updated!')
        else:
            messages.add_message(request, messages.ERROR, 'There was an error updating your comment!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    The view to delete comments on Recipe posts
    """
    queryset = Recipe.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Your comment has been deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete comments you have made!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))