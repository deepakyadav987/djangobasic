from django.contrib import admin
from django.urls import  path
from . import views

urlpatterns = [
    path('<str:name>',views.greet,name="greet"),
    #path('hello/',views.hello,name='hello')
]
