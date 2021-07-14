from django.shortcuts import render, redirect
from .models import Order, CargoItem
#from .forms import OrderForm

# Create your views here.

def index(request):
    items = CargoItem.objects.all()
    context = {'items':items}
    return render(request, 'deliveryco/index.html', context)

def orders(request):
    orders = Order.objects.order_by('dateAdded')
    context = {'orders' : orders}
    return render(request, 'deliveryco/orders.html', context)

def order_particular(request, item_id):

    context = {}

    for item in CargoItem.objects.all():
        if item.itemID == item_id:
            context = {'item':item}

    return render(request, 'deliveryco/order.html', context)

"""
def new_order(request, item_id):
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = OrderForm()

    context = {}

    for item in CargoItem.objects.all():
        if item.itemID == item_id:
            context = {'item':item}

    return render(request, 'deliveryco/new_order.html', context)
"""