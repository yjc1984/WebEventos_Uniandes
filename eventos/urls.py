from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
        url(r'^$', views.lista_eventos),
        url(r'^evento/(?P<pk>[0-9]+)/$', views.detalle_evento, name='detalle_evento'),
    ]
