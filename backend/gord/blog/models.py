from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateField()
    summary = models.TextField()
    outline = models.TextField(blank=True, null=True)
    link = models.URLField()
    likes_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
