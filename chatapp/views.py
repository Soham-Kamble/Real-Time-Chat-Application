from django.shortcuts import render, redirect
from .models import ChatRoom, ChatMessage
from django.utils.text import slugify
from .forms import ChatRoomForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    chatrooms = ChatRoom.objects.all()

    return render(request,'chatapp/index.html',{'chatrooms':chatrooms})

@login_required
def chatroom(request,slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chatroom)[0:30]
    return render(request,'chatapp/room.html',{'chatroom':chatroom,'messages':messages})



def create_room(request):
    if request.method == "POST":
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            base_slug = slugify(room.name)
            slug = base_slug
            counter = 1

            # Ensure unique slug
            while ChatRoom.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            room.slug = slug
            room.save()
            return redirect("chatroom", slug=room.slug)
    else:
        form = ChatRoomForm()
    return render(request, "chatapp/create_room.html", {"form": form})