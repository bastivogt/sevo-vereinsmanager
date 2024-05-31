from django.urls import path

from todos.views import todos
from todos.views import categories

urlpatterns = [
    # todo
    path("todos/", todos.index, name="todos-todo-index"),
    path("todo/create", todos.create, name="todos-todo-create"),
    path("todo/update/<int:id>", todos.update, name="todos-todo-update"),
    path("todo/delete/<int:id>", todos.delete, name="todos-todo-delete"),
    path("todo/detail/<int:id>", todos.detail, name="todos-todo-detail"),
    path("todo/done/<int:id>", todos.done, name="todos-todo-done"),
    path("todo/done/detail/<int:id>", todos.done_from_detail, name="todos-todo-done-detail"),

    # category
    path("categories/", categories.index, name="todos-category-index"),
    path("category/create", categories.create, name="todos-category-create"),
    path("category/update/<int:id>", categories.update, name="todos-category-update"),
    path("category/delete/<int:id>", categories.delete, name="todos-category-delete"),


]