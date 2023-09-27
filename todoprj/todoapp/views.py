from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request, 'todoapp/todo.html', {})

def register(request):
    return render(request, 'todoapp/register.html', {})

def loginpage(request):
    return render(request, 'todoapp/login.html', {})

