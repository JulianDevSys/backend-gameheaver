""" # api/views.py
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Persona
from .serializador import PersonaSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    
 """
 
 # api/views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Persona
from .serializador import PersonaSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
@api_view(['POST'])
def register(request):
    serializer = PersonaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'success'}, status=200)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def login_view(request):
    correo = request.data.get('correo')
    password = request.data.get('password')
    
    if not correo or not password:
        return Response({'error': 'Correo y contraseña son obligatorios.'}, status=400)

    try:
        persona = Persona.objects.get(correo=correo)
        
    except Persona.DoesNotExist:
        return Response({'error': 'El correo no está registrado.'}, status=400)
    
    if persona.check_password(password):
        refresh = RefreshToken.for_user(persona)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        },status=200)
    else:
        return Response({'error': 'Contraseña incorrecta'}, status=400)

@api_view(['GET'])
def datas(request):
    persona= list(Persona.objects.values())
    return JsonResponse(persona,safe=False)