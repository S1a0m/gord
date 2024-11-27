from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    summary = models.TextField()
    link = models.URLField()
    likes_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
