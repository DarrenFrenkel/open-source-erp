from django.db import models
from django.utils.functional import cached_property
# Create your models here.

class Customers(models.Model):
    title = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True) 
    last_name = models.CharField(max_length=200)
    suffix = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    display_name = models.CharField(max_length=200, blank=True)
    print_on_check_as = models.CharField(max_length=200, blank=True)
    billing_street = models.CharField(max_length=200)
    billing_city = models.CharField(max_length=200)
    billing_state = models.CharField(max_length=2)
    billing_zip = models.CharField(max_length=10)
    billing_country = models.CharField(max_length=200) 
    shipping_street = models.CharField(max_length=200, blank=True)
    shipping_city = models.CharField(max_length=200, blank=True)
    shipping_state = models.CharField(max_length=2, blank=True)
    shipping_zip = models.CharField(max_length=10, blank=True)
    shipping_country = models.CharField(max_length=200, blank=True)   
    other_details = models.TextField(blank=True)
       
    def __unicode__(self):  
        return self.first_name + " " + self.last_name 

    def _total_cost_per_customer(self):
        list = []
        for i in self.orders_set.all():
            list.append(i.total)
        total_cost = sum(list) 			
        return total_cost
    total_cost = property(_total_cost_per_customer)

    def print_on_check(self):
        if self.print_on_check_as == None:
            self.print_on_check_as = self.display_name
            return self.print_on_check_as			

class Products(models.Model):
    name = models.CharField(max_length=500) 
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __unicode__(self):  
        return self.name

class Orders(models.Model):
    customer = models.ForeignKey(Customers)
    invoice_number = models.IntegerField()
    invoice_creation_date = models.DateField('Invoice Created Date')
    delivery_due_date = models.DateField('Delivery Due Date')
    payment_due_date = models.DateField('Payment Due Date') 
    custom_message = models.TextField()
    # purchases = models.ManyToManyField(Products, through='Orders_Products')
    
    def __unicode__(self):
        return self.customer.first_name + " " + self.customer.last_name	
	
    def _total(self):
        list = []
        for i in self.orders_products_set.all():
            list.append(i.quantity * i.product.price)
        total_order_cost = sum(list)
        return total_order_cost
    total = property(_total)
	
	
class Orders_Products(models.Model):
    order = models.ForeignKey(Orders)
    product = models.ForeignKey(Products)
    quantity = models.IntegerField(default=0)

    def __unicode__(self):
        return self.product.name
		
    def _cost(self):
        costs = self.quantity * self.product.price
        return costs
    cost = property(_cost)
    		
class General_Settings(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)

class Expenses(models.Model):
    expense_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    date_paid = models.DateField('Expenses Paid Date')
    amount_paid = models.DecimalField(max_digits=20, decimal_places=2)

    def __unicode__(self):  
        return self.expense_name
