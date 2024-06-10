from django.urls import path
from Comment.views import comment
urlpatterns = [
    # 处理一级回复
    path('post_comment/<int:article_id>/', comment.post_comment, name='post_comment'),
    # 处理二级回复
    path('post-comment/<int:article_id>/<int:parent_comment_id>', comment.post_comment, name='comment_reply'),
]