from django.db import models
from django.utils.timezone import now


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, default="", blank=True, null=True, verbose_name="主题")
    published = models.DateTimeField(default=now, verbose_name="创建时间")
    image = models.ImageField(verbose_name="照片", upload_to="media/")
    content = models.TextField(default="", blank=True, null=True, verbose_name="内容")

    def __str__(self):
        return "title:{},  content:{},  updated:{}".format(self.title,
                                                        self.content,
                                                        self.published)

    def summary(self):
        return self.content[:30]


