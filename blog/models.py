from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod, ReadDetail




# 博客类型
class BlogType(models.Model):
    type_name = models.CharField(max_length=15)         # 博客类型名称

    def __str__(self):
        return self.type_name


# 博客信息
class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=50)                                 # 标题
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)    # 博客分类
    content = RichTextUploadingField()                                      # 内容
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)           # 作者
    read_details = GenericRelation(ReadDetail)
    created_time = models.DateTimeField(auto_now_add=True)                  # 创建时间
    last_updated_time = models.DateTimeField(auto_now=True)                 # 编辑时间


    def __str__(self):
        return "<Blog: %s>" % self.title

    class Meta:
        ordering = ['-created_time']













