from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import *
from django.shortcuts import get_object_or_404
from chat.models import Room

# Create your views here.
@login_required(login_url='/login/')
def home_page(request, username):
    user = User.objects.get(username=username)
    advocate = Advocate.objects.get(user=user)
    print('username')
    context = {"User":user, "Advocate":advocate}
    return render(request, 'mainpage.html/', context)

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
            return redirect('/mainpage/'+ username)

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


def add_profile(request):
    if request.method == "POST":
        username = request.POST.get('username')
        practice_areas = request.POST.get('practice_areas')
        experience = request.POST.get('experience')
        advocate_id = request.POST.get('advocate-id')
        location = request.POST.get('location')
        state = request.POST.get('state')
        languages = request.POST.get('languagaes')
        profile_pic = request.POST.get('profile-pic')
        islawyer = request.POST.get('islawyer')
        isadvocate = request.POST.get('isadvocate')
        isarbitrator = request.POST.get('isarbitrator')
        ismediator = request.POST.get('ismediator')
        isnotaries = request.POST.get('isnotaries')
        isdocument_writer = request.POST.get('isdocument_writer')
        bio = request.POST.get('bio')
        case_summary = request.POST.get('case_summary')


        if not User.objects.filter(username = username):
            messages.info(request, "Username does not exist")
            return redirect('/add_update_profile/')
        
        # else:
        #     user = User.objects.get(username = username)
        #     id = user.id

        advocate = Advocate.objects.create(
            practice_areas = practice_areas,
            experience = experience,
            advocate_id = advocate_id,
            location = location,
            state = state,
            languages = languages,
            profile_pic = profile_pic,
            islawyer = islawyer,
            isadvocate = isadvocate,
            isarbitrator = isarbitrator,
            ismediator = ismediator,
            isnotaries = isnotaries,
            isdocument_writer = isdocument_writer,
            bio = bio,
            case_summary = case_summary
        )
        advocate.save()
    return render(request, 'add_profile.html')


# from django.shortcuts import get_object_or_404

def personal_chat(request, username):


    if Room.objects.filter(name=username).exists():
        return redirect('/chat/'+username+'/?username='+username)
    else:
        new_room = Room.objects.create(name=username)
        new_room.save()
        return redirect('/chat/'+username+'/?username='+username)

    return redirect('/chat/' + username)
    

def add_profile(request):
    if request.method == "POST":
        username = request.POST.get('username')
        practice_areas = request.POST.get('practice_areas')
        experience = request.POST.get('experience')
        advocate_id = request.POST.get('advocate-id')
        location = request.POST.get('location')
        state = request.POST.get('state')
        languages = request.POST.get('languages')
        profile_pic = request.FILES.get('profile-pic')
        islawyer = request.POST.get('islawyer')
        isadvocate = request.POST.get('isadvocate')
        isarbitrator = request.POST.get('isarbitrator')
        ismediator = request.POST.get('ismediator')
        isnotaries = request.POST.get('isnotaries')
        isdocument_writer = request.POST.get('isdocument_writer')
        bio = request.POST.get('bio')
        case_summary = request.POST.get('case_summary')

        # Check if the user exists
        user = get_object_or_404(User, username=username)

        # Retrieve the associated Advocate object
        advocate, created = Advocate.objects.get_or_create(user=user)

        # Update the fields with the new data
        advocate.practice_areas = practice_areas
        advocate.experience = experience
        advocate.advocate_id = advocate_id
        advocate.location = location
        advocate.state = state
        advocate.languages = languages
        advocate.profile_pic = profile_pic
        islawyer = islawyer,
        advocate.isadvocate = isadvocate,
        advocate.isarbitrator = isarbitrator,
        advocate.ismediator = ismediator,
        advocate.isnotaries = isnotaries,
        advocate.isdocument_writer = isdocument_writer,
        advocate.bio = bio,
        advocate.case_summary = case_summary

        # Save the changes
        advocate.save()
        # return redirect('add_update_profile/')

    return render(request, 'add_profile.html')

def req(request):
    return render(request, 'req.html')
