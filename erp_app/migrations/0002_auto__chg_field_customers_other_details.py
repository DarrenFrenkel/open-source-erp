# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Customers.other_details'
        db.alter_column(u'erp_app_customers', 'other_details', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'Customers.other_details'
        db.alter_column(u'erp_app_customers', 'other_details', self.gf('django.db.models.fields.CharField')(max_length=500))

    models = {
        u'erp_app.customers': {
            'Meta': {'object_name': 'Customers'},
            'billing_city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'billing_country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'billing_state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'billing_street': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'billing_zip': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'other_details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'print_on_check_as': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'shipping_city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'shipping_country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'shipping_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'shipping_street': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'shipping_zip': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'erp_app.expenses': {
            'Meta': {'object_name': 'Expenses'},
            'amount_paid': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'date_paid': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'expense_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'erp_app.general_settings': {
            'Meta': {'object_name': 'General_Settings'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'erp_app.orders': {
            'Meta': {'object_name': 'Orders'},
            'custom_message': ('django.db.models.fields.TextField', [], {}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp_app.Customers']"}),
            'delivery_due_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_creation_date': ('django.db.models.fields.DateField', [], {}),
            'invoice_number': ('django.db.models.fields.IntegerField', [], {}),
            'payment_due_date': ('django.db.models.fields.DateField', [], {})
        },
        u'erp_app.orders_products': {
            'Meta': {'object_name': 'Orders_Products'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp_app.Orders']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp_app.Products']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'erp_app.products': {
            'Meta': {'object_name': 'Products'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'})
        }
    }

    complete_apps = ['erp_app']