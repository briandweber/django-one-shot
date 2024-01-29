from django.shortcuts import render
from todos.models import TodoList

# Create your views here.
def todolist_list(request):
    lists = TodoList.objects.all()
    context = {
        "lists": lists,
    }
    return render(request, "todos/todolist.html", context)
