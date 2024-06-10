from django import forms
from Article.models import ArticlePost
from mdeditor.fields import MDTextFormField

class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ['title', 'content', 'column', 'tags', 'avatar']





