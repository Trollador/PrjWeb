from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from .forms import RegisterForm, ProfileForm, PartyForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Game, Party, Enter_party, User_profile, Chat
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

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

@login_required
def profile_others(request):
    if request.user.is_active:
        username = request.user.username
        return render (request, 'PartyAssembler/profile_others.html')
    else:
        return redirect('/login')

@login_required
def parties_detail(request, pk):
    party_info = Party.objects.filter(related_game = pk)
    #party = get_object_or_404(Party, pk=pk)
    return render(request, 'PartyAssembler/parties_detail.html', {'party_info': party_info})

@login_required
def enter_party(request, pk):
    enter_party = Enter_party.objects.create(party_has_users=request.user, user_has_parties=Party.objects.get(id = pk))
    enter_party.save()
    integrants = Enter_party.objects.all()
    user = User.objects.all()
    return render(request, 'PartyAssembler/party.html', {'enter_party' : enter_party, 'integrants' : integrants,'user' : user})

    """
 party_list = Enter_party.objects.filter(user_has_parties=Party.objects.get(id = pk))
 users_id = None
    for party in party_list:
        users_id += Enter_party.objects.get(party_has_users)
    """

@login_required
def parties(request):
    all_parties = Party.objects.all()
    return render(request, 'PartyAssembler/parties.html', {'all_parties': all_parties})

@login_required
def update_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit = False)
            form.save()
            return redirect('/profile')
    else:
      form = ProfileForm()
    return render(request, 'PartyAssembler/user_profile.html', {'form' : form})


def baseNav(request):
    user_profile = User_profile.objects.filter(idt = request.user.id)
    user_info = request.user
    return render(request, "PartyAssembler/baseNav.html", {'user_profile': user_profile, 'user_info': user_info })

@login_required
def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, message=msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')

@login_required
def Home(request):
    c = Chat.objects.all()
    return render(request, "PartyAssembler/party.html", {'home': 'active', 'chat': c})

@login_required
def chatTemplate(request):
    c = Chat.objects.all()
    return render(request, "PartyAssembler/chat.html", {'home': 'active', 'chat': c})

@login_required
def Messages(request):
    c = Chat.objects.all()
    return render(request, 'PartyAssembler/messages.html', {'chat': c})
