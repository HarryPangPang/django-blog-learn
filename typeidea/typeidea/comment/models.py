from django.db import models
from blog.models import Post
# Create your models here.

class Base(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    class Meta:
        abstract = True #抽象模型

class Comment(Base):
    nick_name = models.CharField(max_length=50, verbose_name='名称')
    email = models.EmailField(verbose_name='邮箱')
    website = models.URLField(verbose_name='网址')
    content = models.TextField(max_length=255,verbose_name='评论内容')
    target = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='目标')
    
    class Meta:
        verbose_name = verbose_name_plural = '评论'