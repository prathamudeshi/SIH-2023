from django.shortcuts import render, redirect
from chat.models import Room, Message, Documents
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/chat/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/chat/'+room+'/?username='+username)

    # if Room.objects.filter(name = room).exists():
    #     return HttpResponse("Aai zavli")


    # return HttpResponse("Heheheheh")

    # return render(request, 'home.html') 

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def getDocuments(request, room):
    room_details = Room.objects.get(name=room)

    documents = Documents.objects.filter(room=room_details.id)
    return JsonResponse({"documents":list(documents.values())})

def upload_document(request):
    # document = request.POST['document']
    # room_details = Room.objects.get(name=room)

    if request.method == "POST":
        # data=request.POST
        document = request.FILES.get('document') 
        username = request.POST.get('username')
        room_id = request.POST.get('room_id')
        room_details = Room.objects.get(id=room_id)
        room = room_details.name



        # username = data.get('username')
        # room_id = data.get('room_id')

    new_message = Documents.objects.create(value=document, user=username, room=room_id)
    # , user=username, room=room_id
    new_message.save()
    # return HttpResponse('Message sent successfully')
    return redirect('/chat/'+room+'/?username='+username)