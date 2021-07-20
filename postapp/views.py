from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from postapp.models import Post


# Create your views here.
def index(request):
    # return HttpResponse("Hello World!")
    # posts = Post.objects.all()
    posts = Post.objects.order_by("-published").all()

    # posts変数名に関数を指定
    return render(request, "posts/index.html", {"posts": posts})


def page_detail(request):
    id = request.GET.get("id")
    # post = Post.objects.filter(id=id).first()
    post = get_object_or_404(Post, id=id)
    return render(request, "posts/post_detail.html", {"post": post})


def back(request):
    return redirect(to="/")
