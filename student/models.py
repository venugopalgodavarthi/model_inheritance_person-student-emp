from django.db import models

# Create your models here.

class studentmodel(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    li=[['MALE','Male'],['FEMALE','Female']]
    gender=models.CharField(max_length=10,choices=li)
    email=models.EmailField(unique=True)
    phone=models.BigIntegerField(unique=True)
    address=models.CharField(max_length=120,null=True)
    ssc=models.IntegerField()
    puc=models.IntegerField()
    btech=models.IntegerField()
    yop=models.IntegerField()
    course=models.CharField(max_length=50,default='python full stack')
    mock=models.IntegerField(default=2)
    
    
    
    
    
    
    