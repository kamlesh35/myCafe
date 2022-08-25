
from django import forms
from.models import *
   


class OrderdetailsForm(forms.ModelForm):
    
    class Meta:
        model = OrderDetails
        fields = [ 'order_id', 'product_id', 'quantity', 'total_price']
        Widgets = {'order_id':forms.TextInput(attrs = {'class':'form-control'}),
                   'product_id':forms.TextInput(attrs = {'class':'form-control'}),
                   'quantity':forms.TextInput(attrs = {'class':'form-control'}),
                   'total_price':forms.TextInput(attrs = {'class':'form-control'}),
        } 

        
