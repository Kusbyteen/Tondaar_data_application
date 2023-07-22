from django.contrib import admin
from .models import Employee, Supplier, Product, ProductInventory, Buyer, BuyerAddress, Transaction

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'firstname', 'lastname', 'email', 'phone_number', 'department', 'position')
    list_filter = ('department',)
    search_fields = ('firstname', 'lastname', 'email', 'phone_number')

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_id', 'firstname', 'lastname', 'phone_number', 'cooperative_name', 'status')
    list_filter = ('status',)
    search_fields = ('firstname', 'lastname', 'cooperative_name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'unit_price')
    search_fields = ('product_name',)

class ProductInventoryAdmin(admin.ModelAdmin):
    list_display = ('inventory_id', 'product', 'supplier', 'quantity', 'created_at')
    list_filter = ('product', 'supplier', 'created_at')
    search_fields = ('product__product_name', 'supplier__firstname', 'supplier__lastname')

class BuyerAdmin(admin.ModelAdmin):
    list_display = ('buyer_id', 'email', 'business_name', 'firstname', 'lastname', 'phone_number')
    search_fields = ('email', 'business_name', 'firstname', 'lastname', 'phone_number')

class BuyerAddressAdmin(admin.ModelAdmin):
    list_display = ('address_id', 'buyer', 'address_line1', 'city', 'country')
    list_filter = ('city', 'country')
    search_fields = ('buyer__business_name', 'buyer__firstname', 'buyer__lastname', 'address_line1')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'product_name', 'quantity', 'total_amount', 'payment_status', 'delivery_status')
    list_filter = ('payment_status', 'delivery_status')
    search_fields = ('product_name',)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInventory, ProductInventoryAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(BuyerAddress, BuyerAddressAdmin)
admin.site.register(Transaction, TransactionAdmin)

