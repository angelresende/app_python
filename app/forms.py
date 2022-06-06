from django.forms import ModelForm
from app.models import Departamentos, Fornecedores, Users

class DepartamentosForm(ModelForm):
    class Meta:
        model = Departamentos
        fields = ['nome', 'status']

class FornecedoresForm(ModelForm):
    class Meta:
        model = Fornecedores
        fields = ['nome', 'nome_fantasia', 'cnpj', 'inscricao_estadual', 'cep',  'logradouro', 'numero', 'complemento', 'uf', 'localidade', 'telefone', 'email', 'status']

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['nome', 'email', 'senha', 'administrador' , 'status']