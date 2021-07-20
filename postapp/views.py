from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from postapp.models import Post
from postapp.models import TodoModel


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


# Create your views here. 视图函数
# urlsのリクエスと取得後、htmlをレンタリングしウェブブラウザーに表示
def demo(request):
    return render(request, "demo.html")


def todo(request):
    alltodo = TodoModel.objects.all()
    falsetodo = TodoModel.objects.filter(todo_status=False)
    truetodo = TodoModel.objects.filter(todo_status=True)

    print([todo.id for todo in alltodo])
    return render(request, "Todo/todo.html", {"falsetodo": falsetodo, "truetodo": truetodo})


def check_todo(request):
    id = request.GET.get("id")
    # print("id:", id)
    todo = TodoModel.objects.filter(id=id).first()
    if todo:
        todo.todo_status = True
        todo.save()
    else:
        pass
    return redirect(to="../")

    # http://127.0.01.:8000/check_todo/id=3


def pending_todo(request):
    id = request.GET.get("id")
    todo = TodoModel.objects.filter(id=id).first()
    if todo:
        todo.todo_status = False
        todo.save()

    else:
        pass

    return redirect(to="../")


# 优化
def change_todo_states(request):
    id = request.GET.get("id")
    todo = TodoModel.objects.filter(id=id).first()
    print(id, todo.todo_status)
    if todo:
        todo.todo_status = not todo.todo_status  # b = not True --> b = False
        todo.save()

    else:
        pass
    return redirect(to="../")


def delete_todo(request):
    id = request.GET.get("id")
    todo = TodoModel.objects.filter(id=id)
    print(id, todo)
    if todo:
        todo.delete()

    else:
        pass

    return redirect(to="../")


def add_todo(request):
    if not request.method == "POST":
        redirect(to="../")

    title = request.POST.get("title")
    todo = TodoModel()
    todo.title = title
    todo.save()
    return redirect(to="../")
