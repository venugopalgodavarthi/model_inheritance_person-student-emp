from django.http.response import HttpResponse
from django.shortcuts import render
from student.models import studentmodel
# Create your views here.

def register(request):
    if request.method=='POST':
        studentmodel.objects.create(name=request.POST['name'],
                                    age=request.POST['age'],
                                    gender=request.POST['gender'],
                                    address=request.POST['address'],
                                    email=request.POST['email'],
                                    phone=request.POST['phone'],
                                    ssc=request.POST['ssc'],
                                    puc=request.POST['puc'],
                                    btech=request.POST['btech'],
                                    course=request.POST['course'],
                                    yop=request.POST['yop'],
                                    mock=request.POST['mock'])
        return HttpResponse('record is created')
    return render(request,'register.html')

def select(request):
    res=studentmodel.objects.all()
    return render(request,'details.html',{'res':res})

def update(request,data):
    if request.method=='POST':
        studentmodel.objects.filter(id=data).update(name=request.POST['name'],
                                    age=request.POST['age'],
                                    gender=request.POST['gender'],
                                    address=request.POST['address'],
                                    email=request.POST['email'],
                                    phone=request.POST['phone'],
                                    ssc=request.POST['ssc'],
                                    puc=request.POST['puc'],
                                    btech=request.POST['btech'],
                                    course=request.POST['course'],
                                    yop=request.POST['yop'],
                                    mock=request.POST['mock'])
        return HttpResponse('record is update')
    i=studentmodel.objects.get(id=data)
    return render(request,'update.html',{'i':i})

def delete(request,data):
    studentmodel.objects.get(id=data).delete()
    return HttpResponse('record is deleted')
