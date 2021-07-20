"""post URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from postapp.views import index, page_detail, back
from postapp.views import todo, check_todo, pending_todo, change_todo_states, delete_todo, add_todo
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path("page/", page_detail),
    path("back/", back),


    path('todo/change_status/', change_todo_states),
    path('todo/delete_todo/', delete_todo),
    path("todo/add_todo/", add_todo),
    path("todo/", todo)





    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


