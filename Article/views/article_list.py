from django.shortcuts import render
from ..models import ArticlePost
from django.db.models import Q
def article_list(request):
    search = request.GET.get('search')
    order = request.GET.get('order')
    if search:
        if order == 'total_views':
            # 联合查询 |
            articles = ArticlePost.objects.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            ).order_by('-total_views')
        else:
            articles = ArticlePost.objects.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            ).order_by('-total_views')
    else:
        search = ''
        if order =='total_views':
            articles = ArticlePost.objects.all().order_by('-total_views')
            order = 'total_views'
        else:
            articles = ArticlePost.objects.all()
            order = 'normal'
    context = {'articles': articles, 'order': order, 'search': search}
    return render(request, 'article/list.html', context)