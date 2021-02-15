# Generated by Django 3.1.6 on 2021-02-15 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customernumber', models.IntegerField(db_column='customerNumber', primary_key=True, serialize=False)),
                ('customername', models.CharField(db_column='customerName', max_length=50)),
                ('contactlastname', models.CharField(db_column='contactLastName', max_length=50)),
                ('contactfirstname', models.CharField(db_column='contactFirstName', max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('addressline1', models.CharField(db_column='addressLine1', max_length=50)),
                ('addressline2', models.CharField(blank=True, db_column='addressLine2', max_length=50, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('postalcode', models.CharField(blank=True, db_column='postalCode', max_length=15, null=True)),
                ('country', models.CharField(max_length=50)),
                ('creditlimit', models.DecimalField(blank=True, db_column='creditLimit', decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employeenumber', models.IntegerField(db_column='employeeNumber', primary_key=True, serialize=False)),
                ('lastname', models.CharField(db_column='lastName', max_length=50)),
                ('firstname', models.CharField(db_column='firstName', max_length=50)),
                ('extension', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('jobtitle', models.CharField(db_column='jobTitle', max_length=50)),
            ],
            options={
                'db_table': 'employees',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Offices',
            fields=[
                ('officecode', models.CharField(db_column='officeCode', max_length=10, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('addressline1', models.CharField(db_column='addressLine1', max_length=50)),
                ('addressline2', models.CharField(blank=True, db_column='addressLine2', max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(max_length=50)),
                ('postalcode', models.CharField(db_column='postalCode', max_length=15)),
                ('territory', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'offices',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('ordernumber', models.IntegerField(db_column='orderNumber', primary_key=True, serialize=False)),
                ('orderdate', models.DateField(db_column='orderDate')),
                ('requireddate', models.DateField(db_column='requiredDate')),
                ('shippeddate', models.DateField(blank=True, db_column='shippedDate', null=True)),
                ('status', models.CharField(max_length=15)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productlines',
            fields=[
                ('productline', models.CharField(db_column='productLine', max_length=50, primary_key=True, serialize=False)),
                ('textdescription', models.CharField(blank=True, db_column='textDescription', max_length=4000, null=True)),
                ('htmldescription', models.TextField(blank=True, db_column='htmlDescription', null=True)),
                ('image', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'productlines',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('productcode', models.CharField(db_column='productCode', max_length=15, primary_key=True, serialize=False)),
                ('productname', models.CharField(db_column='productName', max_length=70)),
                ('productscale', models.CharField(db_column='productScale', max_length=10)),
                ('productvendor', models.CharField(db_column='productVendor', max_length=50)),
                ('productdescription', models.TextField(db_column='productDescription')),
                ('quantityinstock', models.SmallIntegerField(db_column='quantityInStock')),
                ('buyprice', models.DecimalField(db_column='buyPrice', decimal_places=2, max_digits=10)),
                ('msrp', models.DecimalField(db_column='MSRP', decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orderdetails',
            fields=[
                ('ordernumber', models.OneToOneField(db_column='orderNumber', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='classicmodels.orders')),
                ('quantityordered', models.IntegerField(db_column='quantityOrdered')),
                ('priceeach', models.DecimalField(db_column='priceEach', decimal_places=2, max_digits=10)),
                ('orderlinenumber', models.SmallIntegerField(db_column='orderLineNumber')),
            ],
            options={
                'db_table': 'orderdetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('customernumber', models.OneToOneField(db_column='customerNumber', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='classicmodels.customers')),
                ('checknumber', models.CharField(db_column='checkNumber', max_length=50)),
                ('paymentdate', models.DateField(db_column='paymentDate')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'payments',
                'managed': False,
            },
        ),
    ]