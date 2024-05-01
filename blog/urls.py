from django.urls import path
from . import views
# from django.conf.urls import handler404
# from django.conf.urls import handler500
# from .views import internal_server_error, handle_page_not_found

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('create-recipe', views.RecipeCreate.as_view(), name='recipe_create'),
    path('update-recipe/<slug:slug>', views.RecipeUpdate.as_view(), name='recipe_update'),
    path('recipe-delete/<slug:slug>', views.RecipeDelete.as_view(), name='recipe_delete'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('like/<slug:slug>', views.RecipeLikes.as_view(), name='recipe_likes'),
    path('404/', views.internal_server_error, name='error404'),
    path('500/', views.handle_page_not_found, name='error500'),
]

# handler404 = internal_server_error
# handler500 = handle_page_not_found