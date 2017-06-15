from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from .forms import RegisterForm, ProfileForm, PartyForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Game, Party

def home(request):
    return render_to_response('PartyAssembler/index.html')

@login_required
def games(request):
    img = Game.objects.all().order_by("-id")
    return render_to_response('PartyAssembler/games.html', {'img': img})

def register(request):
        form = RegisterForm(request.POST or None)
        context = {'form':form}
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('/login')
        return render(request, 'PartyAssembler/register.html', context)

def do_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('/games')
    return render(request, 'PartyAssembler/login.html')

def do_logout(request):
    logout(request)
    return redirect('/login')

def user_profile(request):
    if request.method == "POST":
       form = ProfileForm(request.POST)
       if form.is_valid():
        form.save()
        return redirect('/games')
    else:
      form = ProfileForm()
    return render(request, 'PartyAssembler/user_profile.html', {'form' : form})

def create_party(request):
    if request.method == "POST":
       form = PartyForm(request.POST)
       if form.is_valid():
        form.save()
        return redirect('/party')
    else:
      form = PartyForm()
    return render(request, 'PartyAssembler/create_party.html', {'form' : form})
