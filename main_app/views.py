from django.shortcuts import render, redirect
from django.contrib import messages
from login_and_reg_app.models import User
from .models import Wish, Granted

# Create your views here.

def main(request):
    if not 'user_id' in request.session:
        messages.error(request, 'Please log in.')
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'wishes' : user.wishes.all(),
        'granteds' : Granted.objects.all()
    }
    return render(request, 'main.html', context)

def new(request):
    if not 'user_id' in request.session:
        messages.error(request, 'Please log in.')
        return redirect('/')
    return render(request, 'new.html')

def create_wish(request):
    if not 'user_id' in request.session:
        messages.error(request, 'Please log in.')
        return redirect('/')
    errors = Wish.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wishes/new')
    user = User.objects.get(id=request.session['user_id'])
    wish = Wish.objects.create(name=request.POST['name'], description=request.POST['description'], wished_by=user)
    return redirect('/wishes')

def edit(request, wish_id):
    if not 'user_id' in request.session:
        messages.error(request, 'Please log in.')
        return redirect('/')
    wish = Wish.objects.get(id=wish_id)
    context = {
        'wish' : wish
    }
    return render(request, 'edit.html', context)

def edit_wish(request, wish_id):
    if not 'user_id' in request.session:
        messages.error(request, 'Please log in.')
        return redirect('/')
    errors = Wish.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/wishes/edit/{wish_id}')
    wish = Wish.objects.get(id=wish_id)
    wish.name = request.POST['name']
    wish.description = request.POST['description']
    wish.save()
    return redirect('/wishes')

def delete_wish(request, wish_id):
    if not 'user_id' in request.session:
        messages.error(request, 'Please log in.')
        return redirect('/')
    wish = Wish.objects.get(id=wish_id)
    wish.delete()
    return redirect('/wishes')
    
def granted_wish(request, wish_id):
    if not 'user_id' in request.session:
        messages.error(request, 'Please log in.')
        return redirect('/')
    wish = Wish.objects.get(id=wish_id)
    granted = Granted.objects.create(name=wish.name, wished_by=wish.wished_by, og_created_at=wish.created_at)
    wish.delete()
    return redirect('/wishes')