from django.db import models
import uuid


class Pay(models.Model):
    userName = models.CharField(max_length=10, default='client8')
    password = models.CharField(max_length=10, default='1762')
    # orderNumber = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    orderNumber = models.IntegerField(primary_key=True)
    amount = models.IntegerField()
    description = models.CharField(max_length=50)
    returnUrl = models.SlugField(default='/')

    def __str__(self):
        return self.description
