from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList
from todos.forms import TodoListForm

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

def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            model_instance = form.save()
            return redirect("todo_list_detail", id=model_instance.id)
    else:
        form = TodoListForm()
    context = {
        "form": form,
    }
    return render(request, "todos/create.html", context)

def todo_list_update(request, id):
    model_instance = TodoList.objects.get(id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=model_instance)
        if form.is_valid():
            model_instance = form.save()
            return redirect("todo_list_detail", id=model_instance.id)
    else:
        form = TodoListForm(instance=model_instance)

    context = {
        "form": form,
    }
    return render(request, "todos/update.html", context)
