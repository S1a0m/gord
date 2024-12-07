from django.db import models


class Faq(models.Model):
    question = models.CharField(max_length=400)
    response = models.TextField()

    def __str__(self):
        return self.question
