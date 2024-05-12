# In your Django app's admin.py file

from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'vendor', 'date_added')
    list_filter = ('vendor', 'date_added')
    search_fields = ('name', 'vendor')


