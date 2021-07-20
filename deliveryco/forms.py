from django import forms
from .models import Order

class OrderForm(forms.ModelForm):

    orderRecipientFirstName = forms.CharField(label="First Name:", max_length=100)
    orderRecipientLastName = forms.CharField(label="Last Name:", max_length=100)
    orderRecipientAddress = forms.CharField(label="Address:", max_length=200)
    orderRecipientCityName = forms.CharField(label="City:", max_length=100)
    orderRecipientStateName = forms.CharField(label="State:", max_length=100)
    orderRecipientZipCode = forms.IntegerField(label="Zip Code:")
    orderRecipientPhoneNumber = forms.CharField(label="Phone Number:", max_length=100)
    orderRecipientEmail = forms.CharField(label="Email:", max_length=100)

    def __str__(self):
        return orderRecipientLastName

#    class Meta:
#        model = Order

#        fields = ['orderRecipientFirstName', 'orderRecipientLastName', 'orderRecipientAddress', 'orderRecipientCityName', 'orderRecipientStateName', 'orderRecipientZipCode', 'orderRecipientPhoneNumber', 'orderRecipientEmail']

#        labels = {'orderRecipientFirstName':'First Name:', 'orderRecipientLastName':'Last Name:', 'orderRecipientAddress':'Address:', 'orderRecipientCityName':'City:', 'orderRecipientPhoneNumber':'Phone Number:','orderRecipientStateName':'State:', 'orderRecipientZipCode':'Zip Code:', 'orderRecipientEmail': 'Email:'}
