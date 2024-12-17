from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
# Create your views here.

def home(request):
    rooms = Room.objects.all()
    return render(request,'base/home.html',{'rooms':rooms})

def room(request,pk):
    rooms = Room.objects.get(id=pk)
    return render(request,'base/room.html',{"room":rooms})

def createRoom(request):

    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        if not form.is_valid():
            print(form.errors)

    return render(request,'base/room_form.html',{"form":RoomForm()})

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
        if not form.is_valid():
            print(form.errors)
    return render(request,'base/room_form.html',{"room":room,"form":form})