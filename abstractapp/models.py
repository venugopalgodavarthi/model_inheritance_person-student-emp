
from django.db import models

class sample(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    phone=models.BigIntegerField()
    age=models.IntegerField()
    li=[['MALE','Male'],['FEMALE','Female']]
    gender=models.CharField(max_length=10,choices=li)
    address=models.CharField(max_length=100)
    class Meta:
        abstract=True

class student(sample):
    course=models.CharField(max_length=20)
    fee=models.FloatField()
    def __str__(self):
        return str(self.name)
    
class techinal(sample):
    design=models.CharField(max_length=20)
    salary=models.FloatField()
    
class nontechinal(sample):
    design=models.CharField(max_length=20)
    salary=models.FloatField()
    
    