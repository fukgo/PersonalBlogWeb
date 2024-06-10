from django.shortcuts import render
from ..models import ArticlePost
import markdown
from Comment.models import Comment
from Comment.forms import CommentForm
def article_detail(request, id):
    comment_form = CommentForm()
    article = ArticlePost.objects.get(id=id)
    comments = Comment.objects.filter(article=article)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    article.content = markdown.markdown(article.content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    article.total_views+=1
    article.save(update_fields=['total_views'])
    return render(request, 'article/detail.html',
                  {
                   'article': article,
                   'toc': md.toc,
                   'comments': comments,
                   'comment_form': comment_form,
                   }, )
