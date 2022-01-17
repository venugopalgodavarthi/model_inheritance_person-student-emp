from django.contrib import admin
from foreignapp.models import dept,emp
# Register your models here.

class deptadmin(admin.ModelAdmin):
    list_display=['dno','dname','location']

class empadmin(admin.ModelAdmin):
    list_display=['eno','ename','design','salary','email','phone','address','dno']

admin.site.register(dept,deptadmin)
admin.site.register(emp,empadmin)
