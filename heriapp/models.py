from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.BigIntegerField()
    
class student(person):
    course=models.CharField(max_length=30)
    fee=models.IntegerField()
    mock=models.IntegerField()
    
class techinal(person):
    design=models.CharField(max_length=30)
    salary=models.IntegerField()
    
    