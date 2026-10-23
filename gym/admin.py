from django.contrib import admin
from gym import models

# Register your models here.
@admin.register(models.Modality)
class modalityAdmin(admin.ModelAdmin):
    list_display = ("name", "active")
    list_filter = ("active",)

@admin.register(models.Class)
class classAdmin(admin.ModelAdmin):
    list_display = ("modality", "dayOfWeek", "hour", "instructor", "vacancy")
    list_filter = ("modality", "dayOfWeek")
    search_fields = ("instructor",)