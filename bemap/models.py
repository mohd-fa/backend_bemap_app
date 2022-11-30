from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    room = models.CharField(max_length=10)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name
