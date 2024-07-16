from django.contrib.auth.models import User
from django.shortcuts import redirect, render, HttpResponse
from Article.forms import ArticleForm
from ..models import ArticleColumn
from django.contrib.auth.decorators import login_required
@login_required(login_url='/user/login/')
def article_create(request):
    columns = ArticleColumn.objects.all()
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            print('form.is_valid')
            new_article = form.save(commit=False)
            new_article.author = User.objects.get(id=request.user.id)
            new_article.save()
            form.save_m2m()
            return redirect('article_list')
        else:
            form.add_error(None, '表单内容有误，请重新填写')
            return render(request, 'article/create.html', {'form': form, 'columns': columns})
    else:
        form = ArticleForm()
        return render(request, 'article/create.html', {'form': form, 'columns': columns})