from django.urls import path

from . import views

urlpatterns = [
    path("members", views.export_members, name="csv-export-members")
]