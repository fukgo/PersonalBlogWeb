from django.http import HttpResponse
from django import forms
from django.contrib.auth.models import User
from ..forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                form.add_error('username','用户已经存在')
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('article_list')
        else:
            form.add_error(None, '表单内容有误，请重新填写。')
            return render(request, 'user/register.html', {'form': form})

    return render(request, 'user/register.html', {'form': form})
