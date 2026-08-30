from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import EvolutionLineForm
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

#Cadastrar uma nova linha evolutiva
@login_required
def create_line(request):
    
    form = EvolutionLineForm(request.POST or None)
    #Validação do método da requisição
    if request.method == 'POST' and form.is_valid():
        line = form.save(commit=False)
        line.user = request.user #Garantindo que a linha perteça ao usuário
        form.save()    
        
        return redirect('/line/')
    
    return render(request, 'digimon/create_line.html', {'form': form})

#Editar linha evolutiva já criada
@login_required
def update_line(request, id):
    #line recebe o objeto que corresponde ao id e ao usuário que está requisitando
    line = get_object_or_404(
        EvolutionLine,
        id=id,
        user=request.user
    )
    
    if request.method == 'POST':
        form = EvolutionLineForm(request.POST, instance=line)
        if form.is_valid():
            form.save()
        
            return redirect('/line/')
    else:
        form = EvolutionLineForm(instance=line)
    
    return render(request, 'digimon/update_line.html', {'form': form})

#Apagar linha evolutiva
@login_required
def delete_line(request, id):
    #Variável line para receber o objeto obtido com o índice
    line = get_object_or_404(
        EvolutionLine,
        id=id,
        user=request.user
    )
    
    if request.method == 'POST':
        line.delete()
        return redirect('/line/')
    
#Listar linhas evolutivas criadas pelo usuário
@login_required
def list_lines(request):
    #Buscando as linhas que pertencem ao usuário atual
    lines = EvolutionLine.objects.filter(user=request.user)
    
    return render(request, 'digimon/list_lines.html', {'lines': lines})