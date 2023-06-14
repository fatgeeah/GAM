from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Gamer , Games
from .forms import GamerForm

# Create your views here.

def search_games(request):
         if request.method=="POST":
          searched = request.POST['searched']
          allgamers =  Gamer.objects.filter(gamer_games__contains=searched)  
          return render(request, 'system/search_games.html' ,
                        {'searched':searched,
                         'allgamers':allgamers})
         else:
               return render(request, 'system/search_games.html' ,{})


def index(request):
    return render(request, 'system/index.html' , {
        'gamers': Gamer.objects.all()
    })
def games(request):
    allgames = Games.objects.all()
    return render(request, template_name= 'system/games.html' , context={"allgames":allgames})

def view_gamer(request, id):
     gamer = Gamer.objects.get(pk=id)
     return HttpResponseRedirect(reverse('index'))

def add(request):
     if request.method=='POST':

        uname=request.POST.get('username')   
        fname=request.POST.get('firstname') 
        lname=request.POST.get('lastname')
        email=request.POST.get('email') 
        games=request.POST.get('games')  
        my_user=Gamer.objects.create_user(uname,fname,lname,email,games)
        my_user.save()
        print(uname,fname,lname,email,games) 
        return render(request, 'system/add.html')
     
def edit(request, id):
      if request.method =="POST":
       gamer = Gamer.objects.get(pk=id)
       form = GamerForm(request.POST,instance=gamer)
      # if form.is_valid():
      #      form.save()
      return render(request, 'system/edit.html')      

def delete(request, id):
      if request.method =="POST":
       gamer = Gamer.objects.get(pk=id) 
       gamer.delete()
       return HttpResponseRedirect(reverse('index'))           




