from todos.views import todo_list_list, todo_list_detail
from django.urls import path

urlpatterns = [
    path("", todo_list_list, name="todo_list_list"),
    path("<int:id>/todo_list_detail/", todo_list_detail, name="todo_list_detail"),
]
