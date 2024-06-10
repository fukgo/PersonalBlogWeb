from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from Comment.models import Comment
from Article.models import ArticlePost
from ..forms import CommentForm
import markdown
@login_required(login_url='/user/login/')
def post_comment(request, article_id, parent_comment_id=None):
    article = get_object_or_404(ArticlePost, id=article_id)
    comment_form = CommentForm()
    context = {
        'comment_form': comment_form,
        'article_id': article_id,
        'parent_comment_id': parent_comment_id
    }
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form,form.errors)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user
            if parent_comment_id is not None:
                parent_comment = Comment.objects.get(id=parent_comment_id)
                new_comment.parent_id = parent_comment.get_root().id
                new_comment.reply_to = parent_comment.user
                new_comment.save()
                return HttpResponse('200 OK')
            new_comment.save()
            return redirect(article)
            #参数是一个Model对象时，会自动调用这个Model对象的`get_absolute_url()`方法
        else:
            form.add_error(None, '表单内容有误，请重新填写。')
            return render(request, 'comment/reply.html', context)

    return render(request, 'comment/reply.html', context)