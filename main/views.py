from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import *

# Create your views here.
@login_required(login_url='/login/')
def home_page(request):
    return HttpResponse("Finally!!!!!!!!!!!!!!!!!!")

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # email = request.POST.get('email')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
# not User.objects.filter(username=username).exists() or

        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'invalid Password')
            return redirect('/login/')
        
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')
        
def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # islawyer = request.POST.get('islawyer')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already exists.")
            return redirect('/register/')

        user=User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )

        user.set_password(password)
        user.save()

        # if islawyer is "True":
        #     islawyer = bool(True)
        # else:
        #     islawyer = bool(False)

        advocate = Advocate.objects.create(
            user = user,
        )

        advocate.save()

        messages.info(request, "Account created successfully.")
        return redirect('/register/')

    return render(request, 'register.html')

def registerclient(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
      # islawyer = request.POST.get('islawyer')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already exists.")
            return redirect('/register-user/')

        user=User.objects.create(
        first_name = first_name,
        last_name = last_name,
        username = username,
        )

        user.set_password(password)
        user.save()

            # if islawyer is "True":
            #     islawyer = bool(True)
            # else:
            #     islawyer = bool(False)

            # advocate = Advocate.objects.create(
            #     user = user,
            #     islawyer = islawyer,
            # )

            # advocate.save()

        client = Client.objects.create(
            user = user,
        )

        client.save()

        messages.info(request, "Account created successfully.")
        return redirect('/register-user/')

    return render(request, 'registerclient.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')