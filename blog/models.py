from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# 博客类型
class BlogType(models.Model):
    type_name = models.CharField(max_length=15)         # 博客类型名称

    def __str__(self):
        return self.type_name


# 博客信息
class Blog(models.Model):
    title = models.CharField(max_length=50)                                 # 标题
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)    # 博客分类
    content = RichTextUploadingField()                                      # 内容
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)           # 作者

    created_time = models.DateTimeField(auto_now_add=True)                  # 创建时间
    last_updated_time = models.DateTimeField(auto_now=True)                 # 编辑时间

    def __str__(self):
        return "<Blog: %s>" % self.title

    class Meta:
        ordering = ['-created_time']


class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    blog = models.OneToOneField(Blog, on_delete=models.DO_NOTHING)














