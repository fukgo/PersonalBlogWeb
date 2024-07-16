"""
URL configuration for django_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings         # 导入项目文件夹中settings.py模块
from django.views.static import serve    # 导入相关静态文件处理的views控制包
from Article.views import article_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/', include('Article.urls'), name='article'),
    path('user/', include('User.urls'), name='user'),
    path('comment/', include('Comment.urls'), name='comment'),
    #  media配置——配合settings中的MEDIA_ROOT的配置，就可以在浏览器的地址栏访问media文件夹及里面的文件了
    path('', article_list.article_list, name='home')
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
