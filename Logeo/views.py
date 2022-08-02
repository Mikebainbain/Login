from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm #form para crear los registros 

# Create your views here.
def feed(request):
    posts = Post.objects.all()
    return render(request, 'social/feed.html',{"obj":posts})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
    else:
        form = UserCreationForm()
    context = {'form':form}     
    return render(request, 'social/register.html',context)

def profile(request):
    return render(request, 'social/profile.html')