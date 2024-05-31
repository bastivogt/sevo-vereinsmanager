from django.contrib import admin

from . import models

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = [
        "firstname",
        "lastname",
        "birthday",
        "created_at",
        "updated_at"
    ]


admin.site.register(models.Gender)
admin.site.register(models.Position)
admin.site.register(models.Module)
admin.site.register(models.License)
admin.site.register(models.Tariff)
admin.site.register(models.Member, MemberAdmin)
