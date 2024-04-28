from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def price(request):
    return HttpResponse('<h1>How much will it cost--> $60 per month <h1><hr/>')


def your_level(request):
    return HttpResponse('<h1>Your level is--> A1 level<h1><hr/>')