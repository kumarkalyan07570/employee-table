from django.db import models


# Create your models here.
class Employee(models.Model):
    EmployeeID=models.CharField(max_length=100,primary_key=True)
    FastName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Departmentno=models.CharField(max_length=100)


    


class EmployeeDetails(models.Model):
    Departmentno=models.OneToOneField(Employee,on_delete=models.CASCADE)
    Address=models.TextField()
    PhoneNo=models.IntegerField()
    Email=models.EmailField(max_length=254)

class Country(models.Model):
    Country_ID=models.IntegerField(primary_key=True)
    Country_name=models.CharField (max_length=100)

    