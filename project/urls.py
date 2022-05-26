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
from app.views import AdminDepartamentosCreate, AdminDepartamentosIndex, AdminDepartamentosShow, AdminRamaisCreate, AdminRamaisIndex, AdminRamaisShow, AdminUsersCreate, AdminUsersIndex, AdminUsersShow


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('index/', index),
    path('login/', login),
    path('dashboard/', dashboard),
    path('departamentos/criar/', AdminDepartamentosCreate),
    path('departamentos/index/', AdminDepartamentosIndex),
    path('departamentos/show/', AdminDepartamentosShow),
    path('ramais/criar/', AdminRamaisCreate),
    path('ramais/index/', AdminRamaisIndex),
    path('ramais/show/', AdminRamaisShow),
    path('users/criar/', AdminUsersCreate),
    path('users/index/', AdminUsersIndex),
    path('users/show/', AdminUsersShow),
]
