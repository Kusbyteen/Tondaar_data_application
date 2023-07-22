from django.db import models
from django.core.validators import MinValueValidator

# Rest of your model definitions...


class Employee(models.Model):
    staff_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    contract_start_date = models.DateField(blank=True, null=True)
    contract_end_date = models.DateField(blank=True, null=True)
    type_of_employment = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    status = models.SmallIntegerField(choices=((0, 'Active'), (1, 'Inactive')))
    cooperative_name = models.CharField(max_length=100, blank=True, null=True)
    national_card = models.CharField(max_length=50, blank=True, null=True)
    marital_status = models.CharField(max_length=50, blank=True, null=True)
    pwd = models.SmallIntegerField(blank=True, null=True)
    form_of_disability = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    unit_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class ProductInventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)

class Buyer(models.Model):
    buyer_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    business_name = models.CharField(max_length=100, blank=True, null=True)
    identification = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class BuyerAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    modified_at = models.DateTimeField(auto_now=True)

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    total_amount = models.FloatField()
    payment_status = models.CharField(
        max_length=10,
        choices=(('pending', 'Pending'), ('paid', 'Paid'), ('cancelled', 'Cancelled'))
    )
    delivery_status = models.CharField(max_length=20, choices=(('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')))
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    staff = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
