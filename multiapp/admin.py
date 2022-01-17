from django.contrib import admin
from multiapp.models import student,trainer,login
# Register your models here.


class studentadmin(admin.ModelAdmin):
    list_display=['sid','sname','semail','sphone','scourse']
    
admin.site.register(student,studentadmin)

class traineradmin(admin.ModelAdmin):
    list_display=['tid','tname','temail','tphone','tsubject']
admin.site.register(trainer,traineradmin)

class loginadmin(admin.ModelAdmin):
    list_display=['sid','sname','scourse','semail','sphone','tid','tname','tsubject','temail','tphone','insti','batchcode','batch','attendance']
    
admin.site.register(login,loginadmin)
