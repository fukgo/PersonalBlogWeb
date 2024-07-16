from django.db import models
from django.contrib.auth.models import User
from Article.models import ArticlePost
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
from mdeditor.fields import MDTextField
import markdown
class Comment(MPTTModel):
    article = models.ForeignKey(ArticlePost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    #content = models.TextField(),更换为富文本编辑器
    content = MDTextField()
    created = models.DateTimeField(auto_now_add=True)

    # 新增，mptt树形结构
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    # 新增，记录二级评论回复给谁, str
    reply_to = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,related_name='replyers')
    """    class Meta:
        ordering = ('created',)"""
    def __init__(self, *args, **kwargs):
        content = kwargs.pop('content', None)
        super().__init__(*args, **kwargs)
        if content is not None:
            self.content = content
    class MPTTMeat:
        order_insertion_by = ['created']


    def __str__(self):
        return self.content[0:20]
    def content_md(self):
        return markdown.markdown(self.content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])

