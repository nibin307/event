from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Event

def home(request):
    return render(request, 'home.html')

def login_load(request):
    return render(request, 'login.html')

def signup_load(request):
    return render(request, 'signup.html')

def sign_up(request):
    if request.method == 'POST':
        if request.POST['pass'] != request.POST['conpass']:
            return redirect('signup')

        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['pass'],
            first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            email=request.POST['email']
        )
        return redirect('login')

def sign_in(request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['pass']
    )
    if user:
        login(request, user)
        return redirect('show')
    return redirect('login')

def sign_out(request):
    logout(request)
    return redirect('login')

@login_required
def show_events(request):
    return render(request, 'show.html', {'events': Event.objects.all()})

@login_required
def add_event(request):
    if request.method == 'POST':
        Event.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            date=request.POST['date'],
            location=request.POST['location']
        )
        return redirect('show')
    return render(request, 'add.html')

@login_required
def detail_event(request, id):
    return render(request, 'detail.html', {'event': get_object_or_404(Event, id=id)})

@login_required
def edit_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.title = request.POST['title']
        event.description = request.POST['description']
        event.date = request.POST['date']
        event.location = request.POST['location']
        event.save()
        return redirect('show')
    return render(request, 'edit.html', {'event': event})

@login_required
def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
        return redirect('show')
    return render(request, 'delete.html', {'event': event})