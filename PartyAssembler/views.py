from django.shortcuts import render
from PartyAssembler.forms import UserModelForm

def home(request):
    return render(request, 'PartyAssembler/index.html', {})

def register(request):
    form = UserModelForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'PartyAssembler/register.html')
