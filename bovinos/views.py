from django.shortcuts import render, redirect, get_object_or_404
from .models import Boi

def landing_page(request):
    return render(request, 'bovinos/landing.html')

def dashboard(request):
    ultimos_bois = Boi.objects.order_by('-data_cadastro')[:10]
    return render(request, 'bovinos/dashboard.html', {'ultimos_bois': ultimos_bois})

def cadastrar_boi(request):
    if request.method == "POST":
        Boi.objects.create(
            brinco=request.POST.get('brinco'),
            sexo=request.POST.get('sexo'),
            raca=request.POST.get('raca'),
            peso_kg=request.POST.get('peso_kg'),
            data_nascimento=request.POST.get('data_nascimento')
        )
        return redirect('dashboard')
    return render(request, 'bovinos/animal_form.html')

def perfil_boi(request, id):
    boi = get_object_or_404(Boi, id=id)
    return render(request, 'bovinos/animal_detail.html', {'boi': boi})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Boi

def landing_page(request):
    return render(request, 'bovinos/landing.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Loga o usuário direto após criar conta
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'bovinos/registro.html', {'form': form})

# O @login_required impede que entrem sem senha
@login_required
def dashboard(request):
    ultimos_bois = Boi.objects.order_by('-data_cadastro')[:10]
    return render(request, 'bovinos/dashboard.html', {'ultimos_bois': ultimos_bois})

@login_required
def cadastrar_boi(request):
    if request.method == "POST":
        Boi.objects.create(
            brinco=request.POST.get('brinco'),
            sexo=request.POST.get('sexo'),
            raca=request.POST.get('raca'),
            peso_kg=request.POST.get('peso_kg'),
            data_nascimento=request.POST.get('data_nascimento')
        )
        return redirect('dashboard')
    return render(request, 'bovinos/animal_form.html')

@login_required
def perfil_boi(request, id):
    boi = get_object_or_404(Boi, id=id)
    return render(request, 'bovinos/animal_detail.html', {'boi': boi})

    # Coloque isso no final do arquivo bovinos/views.py
@login_required
def assinatura(request):
    return render(request, 'bovinos/assinatura.html')

    from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Boi, HistoricoPeso

def landing_page(request):
    return render(request, 'bovinos/landing.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'bovinos/registro.html', {'form': form})

@login_required
def assinatura(request):
    return render(request, 'bovinos/assinatura.html')

@login_required
def dashboard(request):
    # LÓGICA 2: Filtrar apenas bois ATIVOS para as métricas
    bois_ativos = Boi.objects.filter(status='ATIVO')
    total_cabecas = bois_ativos.count()
    total_machos = bois_ativos.filter(sexo='M').count()
    total_femeas = bois_ativos.filter(sexo='F').count()
    
    ultimos_bois = Boi.objects.order_by('-data_cadastro')[:10]
    
    return render(request, 'bovinos/dashboard.html', {
        'total_cabecas': total_cabecas,
        'total_machos': total_machos,
        'total_femeas': total_femeas,
        'ultimos_bois': ultimos_bois
    })

@login_required
def cadastrar_boi(request):
    if request.method == "POST":
        boi = Boi.objects.create(
            brinco=request.POST.get('brinco'),
            sexo=request.POST.get('sexo'),
            raca=request.POST.get('raca'),
            peso_kg=request.POST.get('peso_kg'),
            data_nascimento=request.POST.get('data_nascimento')
        )
        # Ao cadastrar, cria o primeiro registro de peso no histórico
        HistoricoPeso.objects.create(boi=boi, peso_kg=boi.peso_kg)
        return redirect('dashboard')
    return render(request, 'bovinos/animal_form.html')

@login_required
def perfil_boi(request, id):
    boi = get_object_or_404(Boi, id=id)
    
    # LÓGICA 3: Recebe o formulário de atualização de peso direto na ficha
    if request.method == "POST":
        novo_peso = request.POST.get('novo_peso')
        if novo_peso:
            boi.peso_kg = novo_peso
            boi.save()
            HistoricoPeso.objects.create(boi=boi, peso_kg=novo_peso) # Salva histórico
            return redirect('perfil_boi', id=boi.id)

    historico = boi.historico_peso.all()
    return render(request, 'bovinos/animal_detail.html', {'boi': boi, 'historico': historico})

@login_required
def editar_boi(request, id):
    boi = get_object_or_404(Boi, id=id)
    if request.method == "POST":
        boi.brinco = request.POST.get('brinco')
        boi.status = request.POST.get('status')
        boi.save()
        return redirect('perfil_boi', id=boi.id)
    return render(request, 'bovinos/animal_edit.html', {'boi': boi})