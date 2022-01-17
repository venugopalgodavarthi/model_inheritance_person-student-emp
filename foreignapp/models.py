from enum import unique
from django.db import models

# Create your models here.

class dept(models.Model):
    dno=models.BigAutoField(primary_key=True)
    dname=models.CharField(max_length=30,unique=True)
    location=models.CharField(max_length=30)
    def __str__(self):
        return str(self.dno)
    
class emp(models.Model):
    eno=models.BigAutoField(primary_key=True)
    ename=models.CharField(max_length=40)
    design=models.CharField(max_length=30)
    salary=models.IntegerField()
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.BigIntegerField()
    dno=models.ForeignKey(dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.ename
    