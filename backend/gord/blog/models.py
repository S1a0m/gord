from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateField()
    outline = models.TextField(blank=True, null=True)
    link = models.URLField()
    number_read = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Summary(models.Model):
    blog = models.OneToOneField(BlogPost, on_delete=models.CASCADE, related_name='summary', default=0)
    summary = models.TextField()
    summary_link = models.CharField(max_length=300)

    def __str__(self):
        return f"Sommaire de {self.blog.title}"
