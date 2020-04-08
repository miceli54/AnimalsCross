from django.conf.urls import include, url, path
from . import views

urlpatterns = [
    path('', views.secret, name='secretpage'),
]
