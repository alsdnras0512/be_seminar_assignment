from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        return HttpResponse("200")
    elif request.method == "GET":
        return HttpResponse("200")
    else:
        return HttpResponse("400")
