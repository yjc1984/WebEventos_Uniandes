from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path

from . import views

urlpatterns = [
        url(r'^$', views.lista_eventos),
        url(r'^evento/(?P<pk>[0-9]+)/$', views.detalle_evento, name='detalle_evento'),
        url(r'^evento/nuevo/$', views.evento_nuevo, name='evento_nuevo'),
        url(r'^evento/(?P<pk>[0-9]+)/editar/$', views.editar_evento, name='editar_evento'),
        url(r'^evento/(?P<pk>\d+)/eliminar/$', views.eliminar_evento, name='eliminar_evento'),
        url(r'^signup/$', views.signup, name='signup'),
    ]
