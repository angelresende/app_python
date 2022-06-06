from django.shortcuts import redirect, render
from app.forms import DepartamentosForm, FornecedoresForm, UsersForm
from app.models import Departamentos, Fornecedores, Users

# Create your views here.
def home(request):
    return render(request, 'sobre.html') 

def index(request):
    return render(request, 'index.html') 

def login(request):
    return render(request, 'login.html') 

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

def UsersIndex(request):
    data = {}
    data['db'] = Users.objects.all()
    return render(request, 'users-index.html', data) 

def FormUsers(request):
    data = {}
    data['form'] = UsersForm()
    return render(request, 'users-form.html', data)

def UserCreate(request):
    formUsers = UsersForm(request.POST or None)
    if formUsers.is_valid():
        formUsers.save()
        return redirect('users') 

def UserShow(request, pk):
    data = {}
    data['db'] = Users.objects.get(pk=pk)
    return render(request, 'users-show.html', data) 

def UserEdit(request, pk):
    data = {}
    data['db'] = Users.objects.get(pk=pk)
    data['form'] = UsersForm(instance=data['db'])
    return render(request, 'users-form.html', data) 

def UserUpdate(request, pk):
    data = {}
    data['db'] = Users.objects.get(pk=pk)
    formUsers = UsersForm(request.POST or None, instance=data['db'])
    if formUsers.is_valid():
        formUsers.save()
        return redirect('users') 

def UserDelete(request, pk):
    db = Users.objects.get(pk=pk)
    db.delete()
    return redirect('users') 

