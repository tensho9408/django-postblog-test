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
        return self.content[:100]


# Create your models here. 模型函数

class TodoModel(models.Model):
    title = models.CharField(max_length=32, default="",
                             blank=True,
                             null=True,
                             verbose_name="标题")
    content = models.TextField(default="",
                               blank=True,
                               null=True,
                               verbose_name="具体内容")
    create_time = models.DateTimeField(default=now, verbose_name="创建时间")
    todo_status = models.BooleanField(default=False, verbose_name="处理状态")

    def __str__(self):
        return "标题: {}， 当前处理状态: {}".format(self.title, self.todo_status)

# 代办事项 Todo
# 第一步，设置Model
# # 第二步，页面设置
# 第三步，编辑后端逻辑代码

# MTV- Model, Template, View

# サーバーを起動
# python manage.py run server
# 設定したモデルを登録する
# python manage.py make migrations
# 登録したモデルをデータベースの表に移行する
# python manage.py migrate
# 管理者権権限のユーザーとパスワードを設定
# python manage.py createsuperuser
