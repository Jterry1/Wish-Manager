from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')

def create_user(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode())
    return redirect('/')

def success(request):
    if not 'user_id' in request.session:
        messages.error(request, 'Please log in.')
        return redirect('/')
    return redirect ('/wishes')

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if len(user) == 0:
        messages.error(request, 'Email is incorrect.')
        return redirect('/')
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            request.session['user_first_name'] = logged_user.first_name
            return redirect('/success')
        else:
            messages.error(request, 'Password is incorrect.')
            return redirect('/')
    return redirect("/")

def logout(request):
    request.session.clear()
    return redirect('/')