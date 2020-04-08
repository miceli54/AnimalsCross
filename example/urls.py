from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('secret/', views.secret, name='secretpage'),
]
