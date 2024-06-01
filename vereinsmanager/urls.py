"""
URL configuration for vereinsmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from members.views import members
from seeds import views as seed_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path("", members.redirect, name="index"),
    path("sevo-auth/", include("sevo_auth.urls")),
    path("mbrs/", include("members.urls")),
    path("tds/", include("todos.urls")),
    path("csv-export/", include("csv_export.urls")),
    path("seeds/", include("seeds.urls"))
]
