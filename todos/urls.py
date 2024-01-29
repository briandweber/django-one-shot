from todos.views import todolist_list
from django.urls import path

urlpatterns = [
    path("", todolist_list, name="todolist_list")
]
