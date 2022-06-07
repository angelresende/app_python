from django.db import models

# Create your models here.
class Departamentos(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

class Usuarios(models.Model):
    nome = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=30)
class Fornecedores(models.Model):
    nome = models.CharField(max_length=200)
    nome_fantasia = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    inscricao_estadual = models.CharField(max_length=20)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)
    localidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
