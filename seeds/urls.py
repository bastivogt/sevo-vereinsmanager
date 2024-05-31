from django.urls import path

from . import views

urlpatterns = [
    path("seed/members", views.seed_members, name="seeds-members"),
    path("delete/members/entries/", views.delete_members_entries, name="seeds-delete-members-entries"),

    path("seed/todos", views.seed_todos, name="seeds-todos"),
    path("delete/todos/entries/", views.delete_todos_entries, name="seeds-delete-todos-entries"),

]