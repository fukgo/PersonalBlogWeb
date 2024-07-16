from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate, login
def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            code = form.cleaned_data.get('code')
            if request.session.get('code') != code:
                form.add_error('code', '验证码输入错误')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('article_list')
            else:
                form.add_error('username', '账号或密码输入错误')
                return render(request, 'user/login.html', {'form': form})
        else:
            print(form.errors)
            print(form.cleaned_data)
            form.add_error(None, '输入有误，请检查')
            return render(request, 'user/login.html', {'form': form})
    return render(request, 'user/login.html', {'form': form})

