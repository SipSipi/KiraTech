from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    note = models.TextField(max_length=200)
    stock = models.IntegerField()
    availability = models.BooleanField(default=True)
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,)

    def __str__(self):
        return self.name