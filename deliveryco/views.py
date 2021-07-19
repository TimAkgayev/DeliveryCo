from django.shortcuts import render, redirect
from .models import Order, CargoItem
from .forms import OrderForm

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


def new_order(request, item_id):
    context = {}

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = OrderForm()
        context['item'] = CargoItem.objects.get(itemID=item_id)


    else:
        #POST data submitted; process data.
        form = OrderForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('deliveryco:index')

    #Display a blank or invalid form
    context['form'] = form
    return render(request, 'deliveryco/orderform.html', context)
