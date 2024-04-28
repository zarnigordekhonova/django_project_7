from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def language(request):
    return HttpResponse('<h1>Which language do you want to learn--> French <h1><hr/>')


def months(request):
    return HttpResponse('<h1>How much does it take--> 6 months<h1><hr/>')
