from django.db import models

# Create your models here.
class Article(models.Model):
    text = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.text