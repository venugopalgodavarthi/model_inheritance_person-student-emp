from django.shortcuts import render
from django.http import HttpResponse
from book.models import bookmodel
# Create your views here.


def create(request):
    bookmodel.objects.create(name='django',publish='pyspider',author='girish',dop='2022-1-10',price=500,quantity=500,phone=9966558833, 
     website='www.pyspiders.com')
    
    #res=bookmodel(name='restapi',publish='pyspider',author='venu',dop='2022-1-10',price=500,quantity=500,phone=8866558833, 
     #website='www.pyspiders.com')
    #res.save()
    
    #bookmodel.objects.bulk_create(
     #   [bookmodel(name='sql',publish='pyspider',author='kashi',dop='2022-1-20',
      #             price=500,quantity=500,phone=7766558833, website='www.pyspiders.com'),
       #  bookmodel(name='selenium',publish='pyspider',author='akshay',dop='2022-1-10',
        #           price=500,quantity=300,phone=6666558833, website='www.pyspiders.com')
         #])
    
    return HttpResponse('create a one record')


def select(request):
    res= bookmodel.objects.all()
    #res=bookmodel.objects.filter(price=500)
    #i=bookmodel.objects.get(id=5)
    return render(request,'details.html',{'res':res})


def update(request):
    #res=bookmodel.objects.get(id=5)
    #res.price=2500
    #res.save()
    #bookmodel.objects.filter(quantity=1000).update(price=2000)
    bookmodel.objects.all().update(price=2500)
    return HttpResponse('value is update')


def delete(request):
    #bookmodel.objects.get(id=6).delete()
    #bookmodel.objects.filter(quantity=500).delete()
    #bookmodel.objects.all().delete()
    return HttpResponse('record is delete')