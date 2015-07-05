from django.db import models
from django.core.urlresolvers import reverse


class HelloWorld(models.Model):
    """
    A simple class to demonstrate templates and models
    """
    first_name = models.CharField(max_length=20)
    now = models.DateTimeField()

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.now)

    @staticmethod
    def get_absolute_url():
        return reverse('helloworld:model')
