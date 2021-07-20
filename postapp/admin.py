from django.contrib import admin
from postapp.models import Post, TodoModel
# Register your models here.

admin.site.register(Post)
admin.site.register(TodoModel)