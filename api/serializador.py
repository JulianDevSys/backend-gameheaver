from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Persona
        fields='__all__'
        
    
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        
        persona = Persona.objects.create(**validated_data)
        persona.set_password(password)
        return persona
