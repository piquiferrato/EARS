from rest_framework import serializers, status
from rest_framework.serializers import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import exceptions
from django.conf import settings
from django.utils.translation import gettext as _

# class StudentSerializer(serializers.ModelSerializer):
#     """
#     A student serializer to return the student details
#     """
#     user = UserSerializer(required=True)
#
#     class Meta:
#         model = UnivStudent
#         fields = ('user', 'subject_major',)
#
#

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'password')

class UsuarioSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Usuario
        fields = ('user',
                  'id',
                  'es_tecnico')

    # def create(self, validated_data):
    #     """
    #     Overriding the default create method of the Model serializer.
    #     :param validated_data: data containing all the details of student
    #     :return: returns a successfully created student record
    #     """
    #     user_data = validated_data.pop('user')
    #     user = UserSerializer.create(UserSerializer(), validated_data=user_data)
    #     usuario, created = Usuario.objects.update_or_create(user=user,
    #                         es_tecnico=validated_data.pop('es_tecnico'))
    #     return usuario

# class TecnicoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tecnico
#         fields = ('id',
#                   'email',
#                   'password')


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('id',
                  'tipo_de_pedido',
                  'autor',
                  'tecnico_asignado',
                  'asunto',
                  'detalles',
                  'prioridad',
                  'sistema',
                  'fecha',
                  'archivo_adjunto')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "Usuario desactivado"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Imposible loguear con los parametros dados"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Se necesita el username y password"
            raise exceptions.ValidationError(msg)
        return data
