from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    path('', views.index , name ="home"),
    path('index', views.index , name ="home"),
    path('about', views.about , name ="about"),
    path('contact', views.contact , name ="contact"),
    path('viewMore1', views.viewMore1 , name ="viewMore1"),
    path('viewMore2', views.viewMore2 , name ="viewMore2")
]
