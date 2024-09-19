from django.shortcuts import render

from new.forms import TodoForm
from new.models import Todo


# Create your views here.
# def test(request):
#     return render(request,"test.html")
def demo(request):
    return render(request,"index.html")


def dash(request):
    return render(request,"index1.html")


def test(request):

    data=TodoForm()
    if request.method == "POST":
        todo=TodoForm(request.POST)
        if todo.is_valid():
            todo.save()

    return render(request,"test.html",{"form":data})
def read(request):
    data=Todo.objects.all()
    return render(request,"table.html",{"data":data})
