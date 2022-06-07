from django.forms import ModelForm
from app.models import Departamentos, Fornecedores, Usuarios



class DepartamentosForm(ModelForm):
    class Meta:
        model = Departamentos
        fields = ['nome', 'status']

class FornecedoresForm(ModelForm):
    class Meta:
        model = Fornecedores
        fields = ['nome', 'nome_fantasia', 'cnpj', 'inscricao_estadual', 'cep',  'logradouro', 'numero', 'complemento', 'uf', 'localidade', 'telefone', 'email', 'status']

class UsuariosForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nome', 'email', 'senha', 'administrador' , 'status']


class RegistrarForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['email', 'senha']