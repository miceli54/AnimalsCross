from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.secret, name='secretpage'),
]
