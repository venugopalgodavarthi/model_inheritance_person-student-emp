from django.contrib import admin
from singleapp.models import person,address,payment
# Register your models here.

class personadmin(admin.ModelAdmin):
    list_display=['id','name','age','email','phone']
    
admin.site.register(person,personadmin)


class addressadmin(admin.ModelAdmin):
    list_display=['id','name','age','email','phone','dno','street','city','state','country','pincode']
    
admin.site.register(address,addressadmin)

class paymentadmin(admin.ModelAdmin):
    list_display=['id','name','age','email','phone','dno','street','city','state','country','pincode','accno','accname','db','edate','cvv']
    
admin.site.register(payment,paymentadmin)