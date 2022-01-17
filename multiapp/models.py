from django.db import models

# Create your models here.

class student(models.Model):
    sid=models.BigAutoField(primary_key=True)
    sname=models.CharField(max_length=50)
    semail=models.EmailField()
    sphone=models.BigIntegerField()
    scourse=models.CharField(max_length=20)
    
class trainer(models.Model):
    tid=models.BigAutoField(primary_key=True)
    tname=models.CharField(max_length=50)
    temail=models.EmailField()
    tphone=models.BigIntegerField()
    tsubject=models.CharField(max_length=20)
    
class login(student,trainer):
    insti=models.CharField(max_length=30)
    batchcode=models.CharField(max_length=20)
    attendance=models.IntegerField()
    batch=models.TimeField()
    
    
    