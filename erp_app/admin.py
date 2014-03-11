from django.contrib import admin
from erp_app.models import *

class OrdersInline(admin.TabularInline):
    model = Orders
    extra = 3

class CustomersAdmin(admin.ModelAdmin):
    inlines = [OrdersInline]
	
class OrdersProductsInline(admin.TabularInline):
    model = Orders_Products
    extra = 3

class OrdersAdmin(admin.ModelAdmin):
    inlines = [OrdersProductsInline]	

admin.site.register(Customers, CustomersAdmin)
admin.site.register(Products)
admin.site.register(Orders,OrdersAdmin)
admin.site.register(Orders_Products)
admin.site.register(General_Settings)
admin.site.register(Expenses)

# Register your models here.
