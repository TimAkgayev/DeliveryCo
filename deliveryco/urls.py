from django.urls import path
from . import views

app_name = 'deliveryco'
urlpatterns = [

    #home page
    path('', views.index, name='index'),
    path('orders/', views.orders, name='orders'),
    path('order/<int:item_id>/', views.order_particular, name='order_particular'),
    path('neworder/<int:item_id>/', views.new_order, name='new_order'),
]
