from datetime import datetime

from django.db import models

# Create your models here.
class Transaction(models.Model):
    date= models.DateTimeField(default=datetime.now)
    amount = models.IntegerField(default=0)
    is_income = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)