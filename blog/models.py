from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
