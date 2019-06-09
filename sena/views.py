from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("montemos el proyecto de help desk aca XD")