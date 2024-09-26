from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    data = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title
