from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Base(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    title = models.CharField(max_length=50, verbose_name='标题')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        abstract = True #抽象模型

class Link(Base):
    href = models.URLField(verbose_name='链接')
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1,6),range(1,6)), verbose_name='权重')
    class Meta:
        verbose_name = verbose_name_plural = '友链'


class SideBar(Base):
    SIDE_TYPE = (
        (1, 'HTML'),
        (2, '最新文章'),
        (3, '最热文章'),
        (4, '最新评论')
    )
    display_type = models.PositiveIntegerField(default=1, choices= SIDE_TYPE, verbose_name='展示类型')
    content = models.CharField(max_length=500, blank=True, null=True,verbose_name='内容')

    class Meta:
        verbose_name = verbose_name_plural = '侧边栏'
