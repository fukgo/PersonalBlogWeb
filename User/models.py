# 查看有没有代码错误
from django.contrib.auth.models import User
from django.db import models
# 引入内置信号
from django.db.models.signals import post_save
# 引入信号接收器的装饰器
from django.dispatch import receiver
class Profile(models.Model):

    # 级联删除，也就是当删除主表的数据时候从表中的数据也随着一起删除
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='user/avatars/%Y%m%d/', null=True, blank=True, default='user/avatars/default.jpg')
    introduction = models.TextField(null=True, blank=True, default='无', max_length=120)
    gender_choices = [(0, '女'), (1, '男')]
    gender = models.SmallIntegerField(choices=gender_choices, default=1, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)

    def gender_display(self):
        return self.get_gender_display()

    def __str__(self):
        return '{}'.format(self.user.username)

"""在 User 模型的实例保存后自动管理与其关联的 Profile 实例，确保它们保持同步和一致。"""
# 信号接收函数，每当新建 User 实例时自动调用
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# 信号接收函数，每当更新 User 实例时自动调用
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # 只有当User实例有关联的Profile实例时，Profile实例才会被保存
    if hasattr(instance, 'profile'):
        instance.profile.save()