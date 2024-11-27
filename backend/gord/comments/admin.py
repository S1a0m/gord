from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'email')
    search_fields = ('content', 'email')
    list_filter = ('created_at',)
