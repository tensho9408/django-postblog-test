from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, default="", blank=True, null=True, verbose_name="主题")
    published = models.DateTimeField(default=now, verbose_name="创建时间")
    image = models.ImageField(verbose_name="照片", upload_to="media/", default="", null=True)
    content = models.TextField(default="", blank=True, null=True, verbose_name="内容")
    #author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,default="user")
    # author = models.ForeignKey(User, on_delete=models.CASCADE) 非推奨

    def __str__(self):
        return "title:{}, content:{}, updated:{}".format(self.title,
                                                                    self.content,
                                                                    self.published,
                                                                    )

    def summary(self):
        return self.content[:30]
