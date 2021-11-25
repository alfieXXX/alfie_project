
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

app_name='alfie_app'

urlpatterns = [
    path('', views.home)
]
