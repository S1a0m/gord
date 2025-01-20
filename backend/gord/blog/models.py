from django.db import models
from django.utils.text import slugify


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateField()
    link = models.CharField(max_length=400, blank=True)
    number_read = models.PositiveIntegerField(default=0)
    illustration = models.ImageField(upload_to='illustrations/', null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Générer un slug à partir du titre
        if not self.link:  # Ne pas écraser le lien s'il existe déjà
            self.link = f"{slugify(self.title)}"
        super().save(*args, **kwargs)


class Summary(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='summaries')
    summary = models.TextField()
    summary_link = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return f"Sommaire de {self.blog.title}"

    def save(self, *args, **kwargs):
        # Générer un slug à partir du titre
        if not self.summary_link:  # Ne pas écraser le lien s'il existe déjà
            self.summary_link = f"{slugify(self.summary)}"
        super().save(*args, **kwargs)


class BlogPostSection(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='sections')
    summary = models.OneToOneField(Summary, on_delete=models.CASCADE, related_name='section')
    section_content = models.TextField(blank=True, null=True)
    is_outline = models.BooleanField(default=False)

    def __str__(self):
        return f"Section {self.id} de {self.blog.title}"
