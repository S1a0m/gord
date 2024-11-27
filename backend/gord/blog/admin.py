from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'likes_count')
    search_fields = ('title',)
    list_filter = ('published_date',)
