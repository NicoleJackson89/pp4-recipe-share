from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>', views.recipe_detail, name='recipe_detail'),
    path('add-a-recipe/', views.RecipeCreate.as_view(), name='recipe_create'),
    path('<slug:slug>/edit_comment/<int:comment_id>', 
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('like/<slug:slug>', views.RecipeLikes.as_view(), name='recipe_likes'),
]
