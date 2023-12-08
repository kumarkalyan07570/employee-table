# Generated by Django 4.2.6 on 2023-12-08 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('Country_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Country_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeeID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('FastName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Departmentno', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.TextField()),
                ('PhoneNo', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Departmentno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
            ],
        ),
    ]