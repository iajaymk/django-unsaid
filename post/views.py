
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Message

def home(request):

    message = Message.objects.all().order_by('-date_posted')
    number = Message.objects.count()
    
    context = {
        "messages" : message,
        "numbers" : number,
    }

    return render(request, 'post/index.html',context)


def detail(request,id):

    postnumber = Message.objects.get(pk = id)

    context = {
        "postnumber" : postnumber,
    }

    return render(request, 'post/detail.html', context)


def submit(request):
    if request.method == "POST":
        reciever = request.POST['name']
        messagecontent = request.POST['messagecontent']
        message = Message.objects.create(name=reciever,content=messagecontent)
        
        message.save()

        return redirect('/')
    else:
        return render(request, 'post/submit.html')


def about(request):
    number = Message.objects.count()
    return render(request, 'post/about.html',{'number':number})