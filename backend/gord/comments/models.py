from django.db import models


class Comment(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Liaison à un article ou projet
    content_type = models.CharField(max_length=50)  # "blog" ou "project"
    object_id = models.PositiveIntegerField()
