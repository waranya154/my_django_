from django.shortcuts import render, HttpResponse

# Create your views here.


def index (request):
    return HttpResponse("Hello, World! This is the index page.")


def about (request):
    return HttpResponse("This is the about page.")


def contact (request):
    return HttpResponse("This is the contact page.")