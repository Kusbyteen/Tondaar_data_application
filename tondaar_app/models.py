# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BuyerAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey('Buyers', models.DO_NOTHING)
    address_line1 = models.CharField(max_length=100, blank=True, null=True)
    address_line2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buyer_address'


class Buyers(models.Model):
    buyer_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    business_name = models.CharField(max_length=100, blank=True, null=True)
    identification = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buyers'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    staff_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    contract_start_date = models.DateField(blank=True, null=True)
    contract_end_date = models.DateField(blank=True, null=True)
    type_of_employment = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class ProductInventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_inventory'


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    unit_price = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Suppliers(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    cooperative_name = models.CharField(max_length=100, blank=True, null=True)
    national_card = models.CharField(max_length=50, blank=True, null=True)
    marital_status = models.CharField(max_length=50, blank=True, null=True)
    pwd = models.IntegerField(blank=True, null=True)
    form_of_disability = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suppliers'


class TondaarAppV1Buyer(models.Model):
    buyer_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    business_name = models.CharField(max_length=100, blank=True, null=True)
    identification = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tondaar_app_v1_buyer'


class TondaarAppV1Buyeraddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    modified_at = models.DateTimeField()
    buyer = models.ForeignKey(TondaarAppV1Buyer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tondaar_app_v1_buyeraddress'


class TondaarAppV1Employee(models.Model):
    staff_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    contract_start_date = models.DateField(blank=True, null=True)
    contract_end_date = models.DateField(blank=True, null=True)
    type_of_employment = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tondaar_app_v1_employee'


class TondaarAppV1Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    unit_price = models.FloatField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tondaar_app_v1_product'


class TondaarAppV1Productinventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    product = models.ForeignKey(TondaarAppV1Product, models.DO_NOTHING)
    supplier = models.ForeignKey('TondaarAppV1Supplier', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tondaar_app_v1_productinventory'


class TondaarAppV1Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    status = models.SmallIntegerField()
    cooperative_name = models.CharField(max_length=100, blank=True, null=True)
    national_card = models.CharField(max_length=50, blank=True, null=True)
    marital_status = models.CharField(max_length=50, blank=True, null=True)
    pwd = models.SmallIntegerField(blank=True, null=True)
    form_of_disability = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tondaar_app_v1_supplier'


class TondaarAppV1Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    total_amount = models.FloatField()
    payment_status = models.CharField(max_length=10)
    delivery_status = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    buyer = models.ForeignKey(TondaarAppV1Buyer, models.DO_NOTHING)
    staff = models.ForeignKey(TondaarAppV1Employee, models.DO_NOTHING)
    supplier = models.ForeignKey(TondaarAppV1Supplier, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tondaar_app_v1_transaction'


class Transactions(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField()
    total_amount = models.FloatField()
    payment_status = models.CharField(max_length=9)
    delivery_status = models.CharField(max_length=9)
    supplier = models.ForeignKey(Suppliers, models.DO_NOTHING)
    buyer = models.ForeignKey(Buyers, models.DO_NOTHING)
    staff = models.ForeignKey(Employee, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'
