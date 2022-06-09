from pickle import TRUE
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from app.forms import DepartamentosForm, FornecedoresForm, UsuariosForm, RegistrarForm
from app.models import Departamentos, Fornecedores, Usuarios

# Create your views here.
def home(request):
    return render(request, 'sobre.html') 

def index(request):
    return render(request, 'index.html') 

def index_fornecedores(request):
    data = {}
    data['db'] = Fornecedores.objects.all()
    return render(request, 'index_fornecedores.html', data) 

def index_departamentos(request):
    data = {}
    data['db'] = Departamentos.objects.all()
    return render(request, 'index_departamentos.html', data) 

def login(request):
    data = {}
    data['form'] = RegistrarForm()
    return render(request, 'login.html', data)

def logarSistema(request):
    formLogin = RegistrarForm(request.POST or None)
    if formLogin.is_valid():
        formLogin.save()
        return redirect('dashboard') 


def dashboard(request):
    return render(request, 'dashboard.html')     

def DepartamentosIndex(request):
    data = {}
    data['db'] = Departamentos.objects.all()
    return render(request, 'departamentos-index.html', data) 

def FormDepartamentos(request):
    data = {}
    data['form'] = DepartamentosForm()
    return render(request, 'departamentos-form.html', data)

def DepartamentoCreate(request):
    formDepartamentos = DepartamentosForm(request.POST or None)
    if formDepartamentos.is_valid():
        formDepartamentos.save()
        return redirect('departamentos') 

def DepartamentoShow(request, pk):
    data = {}
    data['db'] = Departamentos.objects.get(pk=pk)
    return render(request, 'departamentos-show.html', data) 

def DepartamentoEdit(request, pk):
    data = {}
    data['db'] = Departamentos.objects.get(pk=pk)
    data['form'] = DepartamentosForm(instance=data['db'])
    return render(request, 'departamentos-form.html', data) 

def DepartamentoUpdate(request, pk):
    data = {}
    data['db'] = Departamentos.objects.get(pk=pk)
    formDepartamentos = DepartamentosForm(request.POST or None, instance=data['db'])
    if formDepartamentos.is_valid():
        formDepartamentos.save()
        return redirect('departamentos') 

def DepartamentoDelete(request, pk):
    db = Departamentos.objects.get(pk=pk)
    db.delete()
    return redirect('departamentos') 

def FornecedoresIndex(request):
    data = {}
    data['db'] = Fornecedores.objects.all()
    return render(request, 'fornecedores-index.html', data) 

def FormFornecedores(request):
    data = {}   
    data['form'] = FornecedoresForm()          
    return render(request, 'fornecedores-form.html', data)

def FornecedorCreate(request):
    formFornecedores = FornecedoresForm(request.POST or None)
    if formFornecedores.is_valid():
        formFornecedores.save()
        return redirect('fornecedores') 

def FornecedorShow(request, pk):
    data = {}
    data['db'] = Fornecedores.objects.get(pk=pk)
    return render(request, 'fornecedores-show.html', data) 

def FornecedorEdit(request, pk):
    data = {}
    data['db'] = Fornecedores.objects.get(pk=pk)
    data['form'] = FornecedoresForm(instance=data['db'])
    return render(request, 'fornecedores-form.html', data) 

def FornecedorUpdate(request, pk):
    data = {}
    data['db'] = Fornecedores.objects.get(pk=pk)
    formFornecedores = FornecedoresForm(request.POST or None, instance=data['db'])
    if formFornecedores.is_valid():
        formFornecedores.save()
        return redirect('fornecedores') 

def FornecedorDelete(request, pk):
    db = Fornecedores.objects.get(pk=pk)
    db.delete()
    return redirect('fornecedores') 

def UsuariosIndex(request):
    data = {}
    data['db'] = Usuarios.objects.all()
    return render(request, 'usuarios-index.html', data) 

def FormUsuarios(request):
    data = {}
    data['form'] = UsuariosForm()
    return render(request, 'usuarios-form.html', data)

def UsuarioCreate(request):
    formusuarios = UsuariosForm(request.POST or None)
    if formusuarios.is_valid():
        formusuarios.save()
        return redirect('usuarios') 

def UsuariosShow(request, pk):
    data = {}
    data['db'] = Usuarios.objects.get(pk=pk)
    return render(request, 'usuarios-show.html', data) 

def UsuarioEdit(request, pk):
    data = {}
    data['db'] = Usuarios.objects.get(pk=pk)
    data['form'] = UsuariosForm(instance=data['db'])
    return render(request, 'usuarios-form.html', data) 

def UsuarioUpdate(request, pk):
    data = {}
    data['db'] = Usuarios.objects.get(pk=pk)
    formusuarios = UsuariosForm(request.POST or None, instance=data['db'])
    if formusuarios.is_valid():
        formusuarios.save()
        return redirect('usuarios') 

def UsuarioDelete(request, pk):
    db = Usuarios.objects.get(pk=pk)
    db.delete()
    return redirect('usuarios') 

def JsonUsuarios(request):
    data = list(Usuarios.objects.values())
    return JsonResponse(data, safe=False)

def JsonDepartamentos(request):
    data = list(Departamentos.objects.values())
    return JsonResponse(data, safe=False)


def JsonFornecedores(request):
    data = list(Fornecedores.objects.values())
    return JsonResponse(data, safe=False)