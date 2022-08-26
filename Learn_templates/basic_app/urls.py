from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from basic_app import views

app_name = 'baseapp'
urlpatterns = [
    path('relative/',views.relative,name="relative"),
    path('other',views.other,name="other"),
]