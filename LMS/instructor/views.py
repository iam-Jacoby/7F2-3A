from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def instructor_dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())