from django.db import models

# Create your models here.

class person(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.BigIntegerField()
    
class address(person):
    dno=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    pincode=models.IntegerField()
    
class payment(address):
    accno=models.BigIntegerField()
    accname=models.CharField(max_length=50)
    db=models.BigIntegerField()
    edate=models.CharField(max_length=10)
    cvv=models.IntegerField()
    
    
    
    
'''  
class person(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.BigIntegerField()
    
class address(person):
    dno=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    pincode=models.IntegerField()
'''
    
