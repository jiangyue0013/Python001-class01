from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello Django!')


def name(request, **kwargs):
    return HttpResponse(kwargs['name'])


def myyear(request, year):
    return render(request, 'yearview.html')


def years(request, year):
    return HttpResponse(year)