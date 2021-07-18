from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        
        fields = ['orderRecipientFirstName', 'orderRecipientLastName', 'orderRecipientBuildingNumber', 'orderRecipientStreetName', 'orderRecipientCityName', 'orderRecipientStateName', 'orderRecipientZipCode', 'orderRecipientPhoneNumber', 'orderRecipientEmail']
        
        labels = {'orderRecipientFirstName':'First Name:', 'orderRecipientLastName':'Last Name:', 'orderRecipientBuildingNumber':'Builing Number:', 'orderRecipientStreetName':'Street Name:', 'orderRecipientCityName':'City:', 'orderRecipientStateName':'State:', 'orderRecipientZipCode':'Zip Code:', 'orderRecipientEmail': 'Email:'}
