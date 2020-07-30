from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def data(request):
    s=datetime.datetime.now()
    return HttpResponse("<h1>Current Date And Tme Is:"+str(s)+"</h1>")
