from django.shortcuts import render
from . models import Message

from django.views.generic import (ListView,CreateView,DetailView)


def home(request):
    messages = Message.objects.all()
    return render(request,'message/index.html',{'messages':messages})


def submit(request):
    if request.method == "POST":
        print('done')


        
        return render(request,'message/index.html')
    else:
        return render(request, 'message/message.html')
            