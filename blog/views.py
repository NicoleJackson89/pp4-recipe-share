from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from .forms import CommentForm


class RecipeList(generic.ListView):
    """
    Returns all published recipes in :model:`blog.Recipe`
    and displays them in a page of 9 posts per page. 
    """
    # queryset = Post.objects.filter(status=1)
    queryset = Recipe.objects.all()
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
    total_comments = recipe.comments.filter(approved=True).count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.success(request, 'Comment submitted and awaiting approval')
            
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
        # {"recipe": recipe,
        #  "coder": "Matt Rudge"},
    )
    

def comment_edit(request, slug, comment_id):
    """
    The view to edit comments in Recipe posts 
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
            messages.success(request, 'Your comment has been Updated and is now awaiting approval!')
        else:
            messages.error(request, 'There was an error updating your comment!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))