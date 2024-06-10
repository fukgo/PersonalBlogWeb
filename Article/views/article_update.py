from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from Article.forms import ArticleForm
from Article.models import ArticlePost, ArticleColumn
from django.contrib.auth.models import User
@login_required(login_url='/user/login/')
def article_update(request, id):
    # pk 实际上是指代主键的通用概念, id只能指主键为id
    article = get_object_or_404(ArticlePost, pk=id)
    columns = ArticleColumn.objects.all()
    # 等同于article = ArticlePost.objects.get(pk=id)
    if request.method == 'POST':
        if request.user != article.author:
            return HttpResponse("抱歉，你无权修改这篇文章。")
        # instance=article 将表单与指定的文章实例关联，这样提交的数据将会应用到这个实例上
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)  # 保存表单数据但不提交到数据库
            if request.FILES.get('avatar'):
                article.avatar = request.FILES.get('avatar')  # 设置文章的 avatar 属性
            if 'tags' in request.POST:
                new_tags = request.POST.get('tags')  # 获取新的标签数据，假设是逗号分隔的字符串
                # 将字符串拆分为标签列表并去除空格
                tag_list = [tag.strip() for tag in new_tags.split(',')]
                # 更新文章的标签
                article.tags.set(tag_list)

            article.save()  # 手动保存 article 对象

            # 返回id知道是文章哪一个
            return redirect('article_detail', id=id)
        else:
            form.add_error(None, '表单内容有误，请重新填写。')
            return render(request, 'article/update.html',
                          {'form': form, 'columns': columns, 'tags': ','.join([x for x in article.tags.names()])})
    else:
        form = ArticleForm(instance=article)
        context = {'article': article, 'form': form, 'columns': columns, 'tags': ','.join([x for x in article.tags.names()])}
        return render(request, 'article/update.html', context)

