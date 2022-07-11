from django.contrib import admin

from todo.models import Task, Tag


@admin.register(Task)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("content",)


@admin.register(Tag)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("name",)
