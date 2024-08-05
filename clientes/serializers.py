from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import * 


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_valido(data['cpf']):
             raise serializers.ValidationError({'cpf':"O número do CPF inválido."})
        
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua numeros nesse campo."})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O RG precisa ter 9 dígitos."})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': "O número de celular deve seguir este modelo 11 44444-4444 (respeitando os espaços)"})
        return data
    