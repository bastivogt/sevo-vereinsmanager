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
        "done_by",
        "created_at",
        "updated_at"

    ]



    list_filter = [
        "created_at",
        "updated_at",
        "categories",
        "done",
        "done_by"
    ]


admin.site.register(models.Todo, TodoAdmin)
admin.site.register(models.Category, CategoryAdmin)

