from rest_framework import serializers
from rest_framework.authtoken.models import Token
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id', 'username', 'es_tecnico')

class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Token
        fields = ('key', 'user',)

class RequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Requisition
        fields = ('id',
                  'type',
                  'author',
                  'assigned_technician',
                  'subject',
                  'details',
                  'priority',
                  'affected_system',
                  'module',
                  'date',
                  'attached_file')
