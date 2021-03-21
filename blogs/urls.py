from django.urls import path
from .import views

#空欄のときはプロジェクトのurlにそのまま飛ぶ
app_name='blogs'
urlpatterns=[
    path('',views.index,name='index'),
    path('detail/<int:blog_id>/',views.detail,name='detail'),
    ]