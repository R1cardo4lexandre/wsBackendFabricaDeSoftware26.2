from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .services.digimon_api import DigimonAPIError, get_digimon, get_digimons
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


@require_POST
def go_to_register(request):
    return redirect('/register/')

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
    levels = (
        ('baby_i_id', 'Baby I'),
        ('baby_ii_id', 'Baby II'),
        ('child_id', 'Child'),
        ('adult_id', 'Adulto'),
        ('perfect_id', 'Perfeito'),
        ('ultimate_id', 'Ultimate'),
        ('super_ultimate_id', 'Super Ultimate'),
    )
    digimon_cache = {}
    api_error = False

    for line in lines:
        line.digimons = []

        for field, level in levels:
            digimon_id = getattr(line, field)
            if not digimon_id:
                continue

            if digimon_id not in digimon_cache:
                try:
                    digimon_cache[digimon_id] = get_digimon(digimon_id)
                except DigimonAPIError:
                    # Mantém a linha visível mesmo se a API estiver indisponível.
                    digimon_cache[digimon_id] = None
                    api_error = True

            digimon = digimon_cache[digimon_id]
            line.digimons.append({
                'level': level,
                'id': digimon_id,
                'name': digimon['name'] if digimon else f'Digimon #{digimon_id}',
            })

    return render(request, 'digimon/list_lines.html', {
        'lines': lines,
        'api_error': api_error,
    })

#View da página inicial, onde estarão listados os digimons da api
def home(request):
    try:
        page = max(int(request.GET.get('page', 0)), 0)
    except (TypeError, ValueError):
        # Trata valores de página inválidos na URL.
        page = 0

    try:
        digimons = get_digimons(page=page, page_size=15)
        api_error = False
    except DigimonAPIError:
        # Evita erro 500 quando a Digi-API não responde.
        digimons = {'content': [], 'last': True}
        api_error = True

    return render(request, 'digimon/home.html', {
        'digimons': digimons,
        'current_page': page,
        'api_error': api_error,
    })
