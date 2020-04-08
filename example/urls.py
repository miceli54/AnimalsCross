from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.secret, name='secretpage'),
]
