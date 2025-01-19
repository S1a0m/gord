from django.db import models


class ProfessionalExperience(models.Model):
    about = models.TextField()
    proof_link = models.URLField(blank=True)

    def __str__(self):
        return self.about


class Testimony(models.Model):
    author_name = models.CharField(max_length=150, blank=True)
    message = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, default='default_avatar.webp')

    def save(self, *args, **kwargs):
        if not self.author_name:
            self.author_name = "Anonyme"
        super().save(*args, **kwargs)
