from django.shortcuts import render
from django.http import HttpResponse

#/menu
def index(request):
    return HttpResponse("Our Pizza")