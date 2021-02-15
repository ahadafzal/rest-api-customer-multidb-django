# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customers(models.Model):
    customernumber = models.TextField(db_column='customerNumber', primary_key=True)  # Field name made lowercase. This field type is a guess.
    customername = models.TextField(db_column='customerName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contactlastname = models.TextField(db_column='contactLastName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contactfirstname = models.TextField(db_column='contactFirstName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    addressline1 = models.TextField(db_column='addressLine1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    addressline2 = models.TextField(db_column='addressLine2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    city = models.TextField(blank=True, null=True)  # This field type is a guess.
    state = models.TextField(blank=True, null=True)  # This field type is a guess.
    postalcode = models.TextField(db_column='postalCode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    country = models.TextField(blank=True, null=True)  # This field type is a guess.
    salesrepemployeenumber = models.TextField(db_column='salesRepEmployeeNumber', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    creditlimit = models.TextField(db_column='creditLimit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'customers'


class Employees(models.Model):
    employeenumber = models.TextField(db_column='employeeNumber', primary_key=True)  # Field name made lowercase. This field type is a guess.
    lastname = models.TextField(db_column='lastName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    firstname = models.TextField(db_column='firstName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    extension = models.TextField(blank=True, null=True)  # This field type is a guess.
    email = models.TextField(blank=True, null=True)  # This field type is a guess.
    officecode = models.TextField(db_column='officeCode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reportsto = models.TextField(db_column='reportsTo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    jobtitle = models.TextField(db_column='jobTitle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'employees'


class Offices(models.Model):
    officecode = models.TextField(db_column='officeCode', primary_key=True)  # Field name made lowercase. This field type is a guess.
    city = models.TextField(blank=True, null=True)  # This field type is a guess.
    phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    addressline1 = models.TextField(db_column='addressLine1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    addressline2 = models.TextField(db_column='addressLine2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    state = models.TextField(blank=True, null=True)  # This field type is a guess.
    country = models.TextField(blank=True, null=True)  # This field type is a guess.
    postalcode = models.TextField(db_column='postalCode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    territory = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'offices'


class Orderdetails(models.Model):
    ordernumber = models.TextField(db_column='orderNumber', primary_key=True)  # Field name made lowercase. This field type is a guess.
    productcode = models.TextField(db_column='productCode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    quantityordered = models.TextField(db_column='quantityOrdered', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    priceeach = models.TextField(db_column='priceEach', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    orderlinenumber = models.TextField(db_column='orderLineNumber', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'orderdetails'


class Orders(models.Model):
    ordernumber = models.TextField(db_column='orderNumber', primary_key=True)  # Field name made lowercase. This field type is a guess.
    orderdate = models.TextField(db_column='orderDate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    requireddate = models.TextField(db_column='requiredDate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    shippeddate = models.TextField(db_column='shippedDate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    comments = models.TextField(blank=True, null=True)  # This field type is a guess.
    customernumber = models.TextField(db_column='customerNumber', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'orders'


class Payments(models.Model):
    customernumber = models.TextField(db_column='customerNumber', blank=True)  # Field name made lowercase. This field type is a guess.
    checknumber = models.TextField(db_column='checkNumber', primary_key=True)  # Field name made lowercase. This field type is a guess.
    paymentdate = models.TextField(db_column='paymentDate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    amount = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'payments'


class Productlines(models.Model):
    productline = models.TextField(db_column='productLine', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    textdescription = models.TextField(db_column='textDescription', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    htmldescription = models.TextField(db_column='htmlDescription', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    image = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'productlines'


class Products(models.Model):
    productcode = models.TextField(db_column='productCode')  # Field name made lowercase. This field type is a guess.
    productname = models.TextField(db_column='productName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    productline = models.TextField(db_column='productLine', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    productscale = models.TextField(db_column='productScale', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    productvendor = models.TextField(db_column='productVendor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    productdescription = models.TextField(db_column='productDescription', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    quantityinstock = models.TextField(db_column='quantityInStock', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyprice = models.TextField(db_column='buyPrice', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    msrp = models.TextField(db_column='MSRP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'products'
