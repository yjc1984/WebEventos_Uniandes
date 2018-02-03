from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
        url(r'^$', views.lista_eventos),
    ]
