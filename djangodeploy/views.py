from django.http.response import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request,'index.html')