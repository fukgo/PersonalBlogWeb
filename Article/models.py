from django.db import models

# Create your models here.
from django.db.models.signals import post_migrate
from django.dispatch import receiver

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from PIL import Image
# 引入imagekit
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from mdeditor.fields import MDTextField
import datetime
class ArticleColumn(models.Model):
    title = models.CharField(max_length=100, blank=True)
    create_time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
@receiver(post_migrate)
def create_default_column(sender, **kwargs):
    if sender.name == 'Article':
        if not ArticleColumn.objects.filter(title='其他').exists():
            ArticleColumn.objects.create(title='其他')
class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = MDTextField()
    # 文章标题图
    avatar = ProcessedImageField(upload_to='article/avatars/%Y%m%d/', blank=True,
                                 processors=[ResizeToFit(width=200)],
                                 format="JPEG",
                                 default='article/avatars/default.jpg',
                                 options={'quality': 100},

                                 )
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(auto_now=True)
    total_views = models.PositiveIntegerField(default=0)

    tags = TaggableManager(blank=True)
    # 文章栏目的 “一对多” 外键
    column = models.ForeignKey(
        ArticleColumn,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='article',
    )

    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ['-update_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.id])

    def was_created_recently(self):
        diff = timezone.now() - self.create_time

        # if diff.days <= 0 and diff.seconds < 60:
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            return True
        else:
            return False


'''    def save(self, *args, **kwargs):
        article = super(ArticlePost, self).save(*args, **kwargs)

        # 固定宽度缩放图片大小
        if self.avatar and not kwargs.get('update_fields'):
            image = Image.open(self.avatar)
            (x, y) = image.size
            new_x = 400
            new_y = int(new_x*(y/x))
            resized_image = image.resize((new_x, new_y), Image.ANTIALIAS)
            resized_image.save(self.avatar.path)
        return article'''

