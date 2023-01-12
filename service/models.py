from django.db import models
from account.models import Profile


class Taxi(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.price}'


class Order(models.Model):
    taxi = models.ForeignKey(Taxi, on_delete=models.CASCADE)
    address = models.CharField(max_length=15)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.taxi} - {self.address}'


class StatusType(models.Model):
    rating = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.raiting}'


class StatusDriver(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    point = models.ForeignKey(StatusType, on_delete=models.CASCADE)

