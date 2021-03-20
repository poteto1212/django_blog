from django.urls import path
from .import views

#空欄
apps_name='blogs'
urlpatterns=[
    path('',views.index,name='index'),
    ]