from rest_framework import serializers
from aplicativo.models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'
        # ['id', 'nome', 'idade', 'sexo', 'cpf']
