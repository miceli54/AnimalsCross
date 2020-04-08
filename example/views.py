from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Oi, is that fish really on land??")
