# snippets/admin.py
from django.contrib import admin
from . models import Task


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('highlighted',)


admin.site.register(Task, TaskAdmin)