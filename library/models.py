from datetime import datetime
from django.db import models


class Book(models.Model):
    add_date = models.DateTimeField(default=datetime.now)
    publish_date = models.DateTimeField(default=datetime.now)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    available = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)