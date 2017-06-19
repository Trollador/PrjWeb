from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from .forms import RegisterForm, ProfileForm, PartyForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Game, Party, Enter_party, User_profile
from django.contrib.auth.models import User

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

@login_required
def reg_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.idt = request.user
            form.save()
            return redirect('/profile')
    else:
      form = ProfileForm()
    return render(request, 'PartyAssembler/user_profile.html', {'form' : form})


def create_party(request):
    if request.method == "POST":
       form = PartyForm(request.POST)
       if form.is_valid():
        form.save()
        return redirect('/games')
    else:
      form = PartyForm()
    return render(request, 'PartyAssembler/create_party.html', {'form' : form})


@login_required
def profile(request):
    try:
        me = User.objects.get(username=request.user.username)
        user = User_profile.objects.get(idt=me)
    except User_profile.DoesNotExist:
        return redirect('/alt-profile')

    if request.user.is_active:
        me = User.objects.get(username=request.user.username)
        userprofile=User_profile.objects.get(idt=me)
        return render(request, 'PartyAssembler/profile.html', {'userprofile' : userprofile})
    else:
        return redirect('/login')

def profile_others(request):
    if request.user.is_active:
        username = request.user.username
        return render (request, 'PartyAssembler/profile_others.html')
    else:
        return redirect('/login')

def parties_detail(request, pk):
    party_info = Party.objects.filter(related_game = pk)
    #party = get_object_or_404(Party, pk=pk)
    return render(request, 'PartyAssembler/parties_detail.html', {'party_info': party_info})

def enter_party(request, pk):
    enter_party = Enter_party.objects.create(party_has_users=request.user, user_has_parties=Party.objects.get(id = pk))
    enter_party.save()
    return render(request, 'PartyAssembler/enter_party.html', {'enter_party' : enter_party})

def parties(request):
    all_parties = Party.objects.all()
    return render(request, 'PartyAssembler/parties.html', {'all_parties': all_parties})
