from django.db import models

# Create your models here.


class bookmodel(models.Model):
    name=models.CharField(max_length=50)
    publish=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    dop=models.DateField()
    price=models.FloatField()
    quantity=models.IntegerField()
    phone=models.BigIntegerField()
    website=models.URLField()
    