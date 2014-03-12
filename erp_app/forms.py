from django import forms
from django.forms import ModelForm
from erp_app.models import Customers

class ExpenseForm(forms.Form):
    name = forms.CharField(max_length=150)
    description = forms.CharField(widget=forms.Textarea(
    attrs={'rows':10, 'cols':30}))
    date_paid = forms.DateField()
    amount_paid = forms.DecimalField()
	
class CustomerForm(ModelForm):

    class Meta:
        model = Customers
        fields = ['title', 'first_name', 'middle_name', 'last_name', 
	    'email', 'company', 'display_name', 'billing_street', 'billing_city', 
	    'billing_state', 'billing_zip', 'billing_country', 'other_details']	
	
	
