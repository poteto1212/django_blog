from django.urls import path
from .import views

apps_name='blogs'
urlpatterns=[
    path('',views.index,name='index'),
    ]