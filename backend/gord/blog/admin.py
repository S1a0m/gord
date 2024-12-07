from django.contrib import admin
from .models import BlogPost, Summary


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    search_fields = ('title',)
    list_filter = ('published_date',)


@admin.register(Summary)
class SummaryAdmin(admin.ModelAdmin):
    list_display = ('summary', 'summary_link')

