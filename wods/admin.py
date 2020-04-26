from django.contrib import admin

from wods.models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_filter = ("name",)
    search_fields = ("id", "name",)
    list_display = ("id", "name")