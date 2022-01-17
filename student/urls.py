from django.urls import path
from student import views
urlpatterns=[
    path('register/',views.register,name='register'),
    path('select/',views.select,name='select'),
    path('update/<data>/',views.update,name='update'),
    path('delete/<data>/',views.delete,name='delete'),
]