from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import EvolutionLineForm

def register(request):
    
    #Cadastro de usuários com validação
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

#Cadastrar uma nova linha evolutiva
@login_required
def create_line(request):
    
    form = EvolutionLineForm(request.POST or None)
    #Validação do método da requisição
    if request.method == 'POST' and form.is_valid():
        line = form.save(commit=False)
        line.user = request.user #Garantindo que a linha perteça ao usuário
        form.save()    
        
        return redirect('create/')
    
    return render(request, 'digimon/create_line.html', {'form': form})
