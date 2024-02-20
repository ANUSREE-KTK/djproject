from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return HttpResponse("hello"),

def about (request):
    return HttpResponse("about page"),

def contact (request):
    return HttpResponse("contact page")
