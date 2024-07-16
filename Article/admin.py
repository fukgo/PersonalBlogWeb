from django.contrib import admin

# Register your models here.
# Register your models here.
from django.contrib import admin
from .models import ArticlePost
from .models import ArticleColumn
admin.site.register(ArticlePost)
admin.site.register(ArticleColumn)