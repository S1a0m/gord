from django.contrib import admin
from .models import Subscriber, Newsletter


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'unsubscribe_token')
    search_fields = ('email',)
    list_filter = ('subscribed_at',)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'subject', 'publish_date', 'status')
    search_fields = ('title',)
    list_filter = ('publish_date',)
