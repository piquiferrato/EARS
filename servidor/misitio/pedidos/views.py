from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User #este es el usuario nativo de django
from rest_framework import viewsets, mixins
from .models import *
from .serializers import *
from rest_framework import generics, permissions
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth import get_user_model

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all().filter(es_tecnico = False)


class TecnicoViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all().filter(es_tecnico = True)


class PedidoViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()

class PedidoMiUsuarioSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all().filter(autor = "2")

class Registrar(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        #  Creando un nuevo usuario
        username = request.POST.get('user.username')
        email = request.POST.get('user.email')
        password = request.POST.get('user.password')
        # es_tecnico = request.POST.get('es_tecnico')
        es_tecnico = False

        user = User.objects.create_user(username, email, password)
        user.save()

        token = Token.objects.create(user=user)

        usuario = Usuario.objects.create(user = user, es_tecnico = es_tecnico)
        usuario.save()

        return Response({'detail': 'El usuario fue creado con el token: ' + token.key})


# class LoginView(mixins.CreateModelMixin, viewsets.GenericViewSet):
#     serializer_class = LoginSerializer
#
#     def create(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data["usuario"]
#         django_login(request, user)
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({"token": token.key}, status=200)


class LogoutView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    authentication_classes = (TokenAuthentication, )

    def create(self, request):
        django_logout(request)
        return Response(status=204)
