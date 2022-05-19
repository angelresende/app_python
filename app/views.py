from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'sobre.html') 

def index(request):
    return render(request, 'index.html') 

def login(request):
    return render(request, 'login.html') 

def AdminDepartamentosIndex(request):
    return render(request, 'admin-departamentos-index.html') 

def AdminDepartamentosCreate(request):
    return render(request, 'admin-departamentos-create.html') 

def AdminDepartamentosShow(request):
    return render(request, 'admin-departamentos-show.html') 

def AdminRamaisIndex(request):
    return render(request, 'admin-ramais-index.html') 

def AdminRamaisCreate(request):
    return render(request, 'admin-ramais-create.html') 

def AdminRamaisShow(request):
    return render(request, 'admin-ramais-show.html') 

def AdminUsersIndex(request):
    return render(request, 'admin-users-index.html') 

def AdminUsersCreate(request):
    return render(request, 'admin-users-create.html') 

def AdminUsersShow(request):
    return render(request, 'admin-users-show.html') 

