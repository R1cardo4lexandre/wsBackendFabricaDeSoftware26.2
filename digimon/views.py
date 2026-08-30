from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import EvolutionLine

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
        