from django.db import models

class HelloWorld(models.Model):
    """
    A simple class to demonstrate templates and models
    """
    first_name = models.CharField(max_length=20)
    now = models.DateTimeField()