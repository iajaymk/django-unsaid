from django.shortcuts import render

def home(request):
    return render(request,'message/index.html')


def submit(request):
    return render(request, 'message/message.html')