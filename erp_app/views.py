from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
import datetime
import time
from django import forms
from erp_app.models import Expenses
from django.template import RequestContext, loader
from django.contrib import messages

from erp_app.models import * 
from erp_app.forms import *

def home(request):
    """View for the Homepage including list of Orders and Expenses""" 
    list_of_orders = Orders.objects.select_related()
    list_of_expenses = Expenses.objects.all()[:5]

    empty_orders = False 
    empty_expenses = False

    if len(list_of_orders) == 0:
        empty_orders = True

    if len(list_of_expenses) == 0:
        empty_expenses = True

    template = 'erp_app/home.html'
    context = RequestContext(request, {'list_of_expenses': list_of_expenses, 
    'list_of_orders': list_of_orders, 'empty_orders': empty_orders,
    'empty_expenses': empty_expenses})
    return render(request, template, context)

def customers(request):
    template = 'erp_app/customers.html'
    form = CustomerForm()	
    orders = Orders.objects.all()
    c = Customers.objects.all()
    list = []
    for i in c:
        list.append(i.total_cost)
	total = sum(list)	
    customers = Customers.objects.all()
    context = RequestContext(request, {'customers':customers, 'orders':orders, 'total':total, 'form':form})
    return render(request, template, context)	

def orders(request):
	pass	

def invoices(request):
	pass	

def products(request):
	pass	

def suppliers(request):
	pass	

def employees(request):
	pass	

def expenses(request):
    """Displays list of Expenses to Expenses template""" 
    list_of_expenses = Expenses.objects.all()

    empty_expenses = False

    if len(list_of_expenses) == 0:
        empty_expenses = True

    form = ExpenseForm()
    template = 'erp_app/expenses.html'
    context = RequestContext(request, {'list_of_expenses': list_of_expenses, 
    'empty_expenses': empty_expenses, 'form': form})
    return render(request, template, context)

def expenses_update(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
    if form.is_valid():
        expense_name = form.cleaned_data['name']
        description = form.cleaned_data['description']
        date_paid = form.cleaned_data['date_paid']
        amount_paid = form.cleaned_data['amount_paid']
        expense = Expenses(expense_name=expense_name, description=description, 
        date_paid=date_paid, amount_paid=amount_paid)
        expense.save()
        return HttpResponseRedirect('/expenses/')
    else:
        list_of_expenses = Expenses.objects.all()                               
        errors = form.errors
        empty_expenses = False                                                      
                                                                                 
        if len(list_of_expenses) == 0:                                              
            empty_expenses = True
                                                        
        template = 'erp_app/expenses.html'                                          
        context = RequestContext(request, {'list_of_expenses': list_of_expenses,    
        'empty_expenses': empty_expenses, 'form': form, 'errors': errors}) 
        return render(request, template, context) 

def reports(request):
	pass	

def taxes(request):
	pass	

def settings(request):
	pass	

def filldb(request):
    """Automatically fills the database with Dummy Data""" 

    # Sets the time
    t = datetime.datetime.now()    

    # Record set 1                                                                  
    e = Expenses(expense_name='Rent', description='Our monthly rent',           
        date_paid=t, amount_paid=500)                                           
    e.save()                                                                    
                                                                                
    p = Products(name='Orange', description='A round fruity ball', price=5)     
    p.save()                                                                    
    product = Products.objects.get(pk=1)                                        
                                                                                
    c = Customers(title='Mr', first_name='OJ', middle_name="Jeremy",            
        last_name="Simpson", suffix="Jr", email="orange@juice.com",             
        company="Slashers Inc", display_name="OJ",                              
        print_on_check_as="OJ Simpson", billing_street="320 Madison Ave",       
        billing_city="San Francisco", billing_state="CA", billing_zip="30284",  
        billing_country="USA", shipping_street="320 Madison Ave",               
        shipping_city="San Francisco", shipping_state="CA",                     
        shipping_zip="30284", shipping_country="USA",                           
        other_details="cant be trusted")                                        
    c.save()                                                                    
    customer = Customers.objects.get(pk=1)                                          
                                                                                
    o = Orders(customer=customer, invoice_number=1, invoice_creation_date=t, 
        delivery_due_date=t, payment_due_date=t, 
        custom_message="Place in the back entrance")        
    o.save()                                                                    
    order = Orders.objects.get(pk=1)                                            
                                                                                
    op = Orders_Products(order=order, product=product, quantity=50)       
    op.save()

    # Record set 2                                                                   
    e = Expenses(expense_name='Electricity',                                    
        description='Our monthly Electricity', date_paid=t,                     
        amount_paid=350.75)
    e.save()

    p = Products(name='Apple', description='Keeps the doctor away', price=4)    
    p.save()
    product = Products.objects.get(pk=2)

    c = Customers(title='Miss', first_name='Heather', middle_name="Peri",       
        last_name="Middleton", suffix="", email="middleton@castle.com",         
        company="Middleton's", display_name="Middleton's",                           
        print_on_check_as="Middleton's", billing_street="520 Terracotta Ave",      
        billing_city="England", billing_state="UK", billing_zip="73329",        
        billing_country="UK", shipping_street="520 Terracotta Ave",             
        shipping_city="England", shipping_state="UK", shipping_zip="73329",     
        shipping_country="UK", other_details="possibly royalty")                
    c.save()
    customer = Customers.objects.get(pk=2)

    o = Orders(customer=customer, invoice_number=2, invoice_creation_date=t, delivery_due_date=t,       
        payment_due_date=t, custom_message="Give the cheese to Sam")            
    o.save()
    order = Orders.objects.get(pk=2)

    op = Orders_Products(order=order, product=product, quantity="35") 
    op.save()


    # Record set 3
    e = Expenses(expense_name='Gas',                                            
        description='Our monthly Gas', date_paid=t,                             
        amount_paid=275.15)
    e.save()

    p = Products(name='Apple', description='Keeps the doctor away', price=4)
    p.save()
    product = Products.objects.get(pk=3)

    c = Customers(title='Mr', first_name='Herbert', middle_name="",       
        last_name="Shrute", suffix="", email="shrute@beets.com",         
        company="Shrute's Beets", display_name="Shrute's Beets",                           
        print_on_check_as="Shrute's Beets", billing_street="1100 Farm Lane",      
        billing_city="Louiseville", billing_state="CO", billing_zip="80224",        
        billing_country="USA", shipping_street="1100 Farm Lane",             
        shipping_city="Louiseville", shipping_state="CO", shipping_zip="80224",     
        shipping_country="USA", other_details="Eats too many beets")
    c.save()
    customer = Customers.objects.get(pk=3)

    o = Orders(customer=customer, invoice_number=3, invoice_creation_date=t, 
        delivery_due_date=t, payment_due_date=t, 
        custom_message="Give the cheese to Sam")
    o.save()
    order = Orders.objects.get(pk=3)

    op = Orders_Products(order=order, product=product, quantity="35")
    op.save()
                                                                     
    # Record set 4                                                                            
    e = Expenses(expense_name='Land Tax', description='Our monthly Land Tax',   
        date_paid=t, amount_paid=146.23)
    e.save()

    p = Products(name='Rubix Cube', description='A puzzling square', price=20)
    p.save()
    product = Products.objects.get(pk=4)

    c = Customers(title='Mr', first_name='John', middle_name="",                
        last_name="Prescott", suffix="", email="john@prescott.com",             
        company="Prescott's", display_name="Prescott's",                        
        print_on_check_as="Prescott's", billing_street="12 Richy Lane",         
        billing_city="Hoboken", billing_state="NY", billing_zip="54109",        
        billing_country="USA", shipping_street="12 Richy Lane",                 
        shipping_city="Hoboken", shipping_state="NY", shipping_zip="54109",     
        shipping_country="USA", 
        other_details="Extremely loyal to our brand. Don't know why")
    c.save()
    customer = Customers.objects.get(pk=4)

    o = Orders(customer=customer, invoice_number=4, invoice_creation_date=t, 
        delivery_due_date=t, payment_due_date=t, 
        custom_message="Send Rubix Cubes to everyone")
    o.save()
    order = Orders.objects.get(pk=4)
    
    op = Orders_Products(order=order, product=product, quantity="12")
    op.save()

    # Record set 5                                                                            
    e = Expenses(expense_name='Exterminators', description='Pest Control',   
        date_paid=t, amount_paid=1200.73)
    e.save()

    p = Products(name='Tissues', description='Snot paper', price=3.75)
    p.save()
    product = Products.objects.get(pk=5)

    c = Customers(title='Mr', first_name='Harry', middle_name="",                
        last_name="Houdini", suffix="", email="escape@thebox.com",             
        company="Escapists", display_name="Escapists",                        
        print_on_check_as="Escapists", billing_street="820 Shift Place",         
        billing_city="London", billing_state="England", billing_zip="23949",        
        billing_country="UK", shipping_street="820 Shift Place",                 
        shipping_city="London", shipping_state="England", shipping_zip="23949",     
        shipping_country="UK", 
        other_details="Can escape out of any contract. Beware!")
    c.save()
    customer = Customers.objects.get(pk=5)

    o = Orders(customer=customer, invoice_number=4, invoice_creation_date=t, 
        delivery_due_date=t, payment_due_date=t, 
        custom_message="Put him in a water-filled box to complete delivery")
    o.save()
    order = Orders.objects.get(pk=5)
    
    op = Orders_Products(order=order, product=product, quantity="12")
    op.save()

    template = 'erp_app/filldb.html'
    return render(request, template)


def wipedb(request):
    Customers.objects.all().delete()
    Products.objects.all().delete()
    Orders.objects.all().delete()
    Orders_Products.objects.all().delete()
    General_Settings.objects.all().delete()
    Expenses.objects.all().delete()

    template = 'erp_app/wipedb.html'                                            
    return render(request, template)
