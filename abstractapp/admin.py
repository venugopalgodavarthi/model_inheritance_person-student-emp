from django.contrib import admin
from abstractapp.models import student,techinal,nontechinal
# Register your models here.



class studentadmin(admin.ModelAdmin):
    list_display=['id','name','email','phone','age','gender','address','course','fee']
    
admin.site.register(student,studentadmin)

class techinaladmin(admin.ModelAdmin):
    list_display=['id','name','email','phone','age','gender','address','design','salary']
    
admin.site.register(techinal,techinaladmin)

class nontechinaladmin(admin.ModelAdmin):
    list_display=['id','name','email','phone','age','gender','address','design','salary']
    
admin.site.register(nontechinal,nontechinaladmin)

