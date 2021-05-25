from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Wallet(models.Model):
    owner = models.OneToOneField(to=User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    dob = models.DateField()
    proof = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    balance = models.FloatField(default=0)

    def __str__(self):
        return self.owner.username + "'s wallet"


class Transaction(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=100)
    amount = models.FloatField()
    expense = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    date = models.DateField(default=timezone.now)

    class Meta:
        ordering: ['date']

    def __str__(self):
        return self.owner.username + "'s Transaction"
