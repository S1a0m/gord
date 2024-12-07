from django.db import models
import uuid


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    unsubscribe_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    DRAFT = 'draft'
    SENT = 'sent'
    STATUS_CHOICES = [
        (DRAFT, 'Brouillon'),
        (SENT, 'Envoyée'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    subject = models.CharField(max_length=255)
    publish_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=DRAFT)
    subscribers = models.ManyToManyField(Subscriber)
    preview_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
