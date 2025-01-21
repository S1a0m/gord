from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'release_date', 'status')
    search_fields = ('name',)
    list_filter = ('release_date',)

