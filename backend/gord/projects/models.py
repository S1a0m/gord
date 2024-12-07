from django.db import models


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('dev', 'Development'),
        ('cyber', 'Cybersecurity'),
        ('ia', 'Artificial Intelligence'),
        ('math', 'Mathematics'),
        ('elec', 'Electronic')
        # Ajoute d'autres catégories ici
    ]
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    summary = models.TextField()
    link = models.URLField()
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='dev'  # Catégorie par défaut
    )
    number_read = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

