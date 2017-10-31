from django.shortcuts import render
from __future__ import unicode_literals
# Create your views here.
def menu(request):
    if(request.method=='GET'):
        return render(request,'menu.html')
