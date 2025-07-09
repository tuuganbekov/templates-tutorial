from django.db import models

# Create your models here.

class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name
