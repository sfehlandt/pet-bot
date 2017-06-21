from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^run$', views.index, name='index'),
    url(r'^db', views.db, name='db'),
]
