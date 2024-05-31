from django.urls import path

from . import views

urlpatterns = [
    path("seed/", views.index, name="seeds-index"),
    path("delete/members/entries/", views.delete_members_entries, name="seeds-delete-members-entries"),
]