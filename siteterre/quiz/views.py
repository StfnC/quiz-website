from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>This is working!</h1>')
