from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render_to_response('PartyAssembler/index.html')

@login_required
def games(request):
    return render(request, 'PartyAssembler/games.html')

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
