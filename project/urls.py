"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import home, index, login,dashboard 
from app.views import DepartamentosIndex, FormDepartamentos, DepartamentoCreate, DepartamentoShow, DepartamentoEdit, DepartamentoUpdate, DepartamentoDelete
from app.views import FornecedoresIndex, FormFornecedores, FornecedorCreate, FornecedorShow, FornecedorEdit, FornecedorUpdate, FornecedorDelete
from app.views import UsuariosIndex, FormUsuarios, UsuarioCreate, UsuariosShow, UsuarioEdit, UsuarioUpdate, UsuarioDelete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('departamentos/', DepartamentosIndex, name='departamentos'),
    path('departamentos_form/',FormDepartamentos , name='departamentos_form'),  
    path('criar_departamento/',DepartamentoCreate, name='criar_departamento'),      
    path('visualizar_departamento/<int:pk>/', DepartamentoShow, name='visualizar_departamento'),
    path('editar_departamento/<int:pk>/', DepartamentoEdit, name='editar_departamento'),
    path('atualizar_departamento/<int:pk>/', DepartamentoUpdate, name='atualizar_departamento'),
    path('deletar_departamento/<int:pk>/', DepartamentoDelete, name='deletar_departamento'),
    path('fornecedores/', FornecedoresIndex, name='fornecedores'),
    path('fornecedores_form/',FormFornecedores , name='fornecedores_form'),  
    path('criar_fornecedor/',FornecedorCreate, name='criar_fornecedor'),      
    path('visualizar_fornecedor/<int:pk>/', FornecedorShow, name='visualizar_fornecedor'),
    path('editar_fornecedor/<int:pk>/', FornecedorEdit, name='editar_fornecedor'),
    path('atualizar_fornecedor/<int:pk>/', FornecedorUpdate, name='atualizar_fornecedor'),
    path('deletar_fornecedor/<int:pk>/', FornecedorDelete, name='deletar_fornecedor'),
    path('usuarios/', UsuariosIndex, name='usuarios'),
    path('usuarios_form/',FormUsuarios , name='usuarios_form'),  
    path('criar_usuario/', UsuarioCreate, name='criar_usuario'),      
    path('visualizar_usuario/<int:pk>/', UsuariosShow, name='visualizar_usuario'),
    path('editar_usuario/<int:pk>/', UsuarioEdit, name='editar_usuario'),
    path('atualizar_usuario/<int:pk>/', UsuarioUpdate, name='atualizar_usuario'),
    path('deletar_usuario/<int:pk>/', UsuarioDelete, name='deletar_usuario'),
]
