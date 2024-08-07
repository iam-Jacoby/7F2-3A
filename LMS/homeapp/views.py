from django.shortcuts import render
from django.http import HttpResponse

def temporary(request):
    return HttpResponse("Hello world!")