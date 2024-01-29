from django.shortcuts import render, get_object_or_404
from todos.models import TodoList

# Create your views here.
def todo_list_list(request):
    lists = TodoList.objects.all()
    context = {
        "lists": lists,
    }
    return render(request, "todos/list.html", context)

def todo_list_detail(request, id):
    list = get_object_or_404(TodoList, id=id)
    context = {
        "list_object": list,
    }
    return render(request, "todos/todo_list_detail.html", context)
