from django.db import models
from django.contrib.auth.models import User # user模块使用自带的
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

class Category(Base):
    name = models.CharField(max_length=50, verbose_name='名称')
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = '分类'
    
class Tag(Base):
    name = models.CharField(max_length=10, verbose_name='标签')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = '标签'

class Post(Base):
    title = models.CharField(max_length=255, verbose_name='标题')
    desc = models.CharField(max_length=1025, verbose_name='摘要')
    content = models.TextField(verbose_name='正文', help_text='必须是MD格式')
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id'] #根据id降序排列q

