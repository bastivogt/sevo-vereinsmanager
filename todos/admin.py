from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "created_at",
        "updated_at"
    ]

class TodoAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "user", 
        "created_at",
        "updated_at"

    ]


admin.site.register(models.Todo, TodoAdmin)
admin.site.register(models.Category, CategoryAdmin)

