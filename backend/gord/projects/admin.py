from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'likes_count')
    search_fields = ('name',)
    list_filter = ('release_date',)
