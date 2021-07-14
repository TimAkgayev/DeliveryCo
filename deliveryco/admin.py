from django.contrib import admin
from .models import Order, Truck, CargoItem

# Register your models here.

admin.site.register(Order)
admin.site.register(Truck)
admin.site.register(CargoItem)