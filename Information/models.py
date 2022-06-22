from ast import Not
from audioop import minmax
from unicodedata import name
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    card = models.IntegerField()
    merit = models.CharField(max_length=2000, null=True)
    info = models.CharField(max_length=10000, null=True)
    trained = models.ManyToManyField("Trained")

    def __str__(self):
        return f"{self.name} {self.surname} {self.card} {self.info} {self.merit} {self.trained}"

class Trained(models.Model):
    name = models.CharField(max_length=50)
    done = models.BooleanField(null=True)
    
    def traineds(self):
        return ", ".join(str(trained) for trained in Employee.objects.filter(trained = self))

    def __str__(self):
        return f"{self.name}"