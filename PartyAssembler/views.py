from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render_to_response('PartyAssembler/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
        else:
            return render(request, 'PartyAssembler/register.html', {'form': form})
    return render(request, 'PartyAssembler/register.html', {'form': RegisterForm()})

def do_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = authenticate(apelido=request.POST['apelido'], password=request.POST['senha'])
        if user is not None:
            login(request, user)
            return redirect('/games')
    return render(request, 'PartyAssembler/login.html', {'form': LoginForm()})

def do_logout(request):
    logout(request)
    return redirect('/login')
