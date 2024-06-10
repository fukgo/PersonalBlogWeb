from django.urls import path, include
from Article.views import article_list, article_detail, article_create
from Article.views.article_delete import article_delete
from Article.views.article_update import article_update
from Article.views.create_column import create_column

urlpatterns = [
    path('list/', article_list.article_list, name='article_list'),
    path('detail/<int:id>/', article_detail.article_detail, name='article_detail'),
    path('create/', article_create.article_create, name='article_create'),
    path('delete/<int:id>/', article_delete, name="article_delete"),
    path('update/<int:id>/', article_update, name='article_update'),
    path('add_cloumn/', create_column, name='add_column'),
]
