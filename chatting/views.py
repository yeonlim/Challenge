from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .forms import *
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# Create your views here.

def chatting(request):
    messages = Message.objects.filter(to=request.user).order_by('-id')
    paginator = Paginator(messages, 5)
    page = request.GET.get('page')
    message = paginator.get_page(page)
    return render(request, "chatting_main.html", {'message':message})

def chatting_send(request):
    messages =Message.objects.filter(writer=request.user).order_by('-id')
    paginator = Paginator(messages, 5)
    page = request.GET.get('page')
    message = paginator.get_page(page)
    return render(request,"chatting_send.html", {'message':message})

def chatting_write(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.writer = request.user
            message.pub_date = timezone.now() 
            message.save()
            return redirect("chatting")
    else:
        form = MessageForm()
        return render(request, 'chatting_write.html', {'form':form})

def chatting_userlist(request):
    users = get_user_model().objects.all().order_by('-username')
    print(users)
    return render(request, 'userlist.html', {'users':users})

def chatting_detail(request, id): 
    message = get_object_or_404(Message, pk=id) 
    return render(request, 'chatting_detail.html', {'message':message})

def chatting_delete(request, id): 
    delete_message = get_object_or_404(Message, pk=id)
    delete_message.delete()
    return redirect('chatting')      



    