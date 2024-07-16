from ..models import ArticlePost
from django.shortcuts import render, redirect
def article_delete(request, id):
    ArticlePost.objects.get(id=id).delete()
    return redirect('article_list')



