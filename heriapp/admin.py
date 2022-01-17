from django.contrib import admin

# Register your models here.
from heriapp.models import person,student,techinal
# Register your models here.

class personadmin(admin.ModelAdmin):
    list_display=['id','name','age','email','phone']
    
admin.site.register(person,personadmin)


class studentadmin(admin.ModelAdmin):
    list_display=['id','name','age','email','phone','course','fee','mock']
    
admin.site.register(student,studentadmin)

class techinaladmin(admin.ModelAdmin):
    list_display=['id','name','age','email','phone','design','salary']
admin.site.register(techinal,techinaladmin)
