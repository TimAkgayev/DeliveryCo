from django.db import models

# Create your models here.


class Order(models.Model):
    orderName = models.CharField(max_length = 50)
    orderNumber = models.AutoField(primary_key = True)
    dateAdded = models.DateTimeField(auto_now_add=True)

    orderRecipientFirstName = models.CharField(max_length = 50, null=True, blank=True)
    orderRecipientLastName = models.CharField(max_length = 50, null=True, blank=True)
    orderRecipientBuildingNumber = models.IntegerField(null=True, blank=True)
    orderRecipientStreetName = models.CharField(max_length = 50, null=True, blank=True)
    orderRecipientCityName = models.CharField(max_length = 50, null=True, blank=True)
    orderRecipientStateName = models.CharField(max_length = 20, null=True, blank=True)
    orderRecipientZipCode = models.IntegerField(null=True, blank=True)
    orderRecipientPhoneNumber = models.IntegerField(null=True, blank=True)
    orderRecipientEmail = models.CharField(max_length = 100, null=True, blank=True)

    def __str__(self):
        return self.orderName

class Truck(models.Model):
    truckModel = models.CharField(max_length = 50)
    truckNumber = models.IntegerField()
    maxCarryingCapacity = models.IntegerField()


    def __str__(self):
        return self.truckModel

class CargoItem(models.Model):
    itemName = models.CharField(max_length = 50)
    itemDescription = models.TextField()
    itemID = models.AutoField(primary_key = True)
    itemWeight = models.IntegerField()
    itemImage = models.ImageField()
    inventoryCount = models.IntegerField()
   # assignedTruck = models.ForeignKey(Truck, blank = True, null = True, on_delete = models.PROTECT)
   # assignedOrder = models.ForeignKey(Order, blank = True, null = True, on_delete = models.PROTECT)

    def __str__(self):
        return self.itemName
