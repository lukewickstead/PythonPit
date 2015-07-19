from django.db import models
from django.db.models import Model


class Quote(Model):
    quote = models.TextField()
    author = models.CharField(max_length=50)

    def __str__(self):
        return "{0}: {1}".format(self.author, self.quote)
