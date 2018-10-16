from rest_framework import serializers
from rest_framework.authtoken.models import Token
from . import models

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
<<<<<<< HEAD
=======
        ordering = ['priority']


class UserSerializer(serializers.ModelSerializer):
    # author = RequisitionSerializer(many=True, read_only=True)
    class Meta:
        model = models.CustomUser
        fields = ('id', 'username', 'es_tecnico', 'author')
        # fields = ('id', 'username', 'es_tecnico', 'author')

class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Token
        fields = ('key', 'user',)

class UserSerializer2(serializers.ModelSerializer):
    author = RequisitionSerializer(many=True, read_only=True)
    class Meta:
        model = models.CustomUser
        fields = ('id','author')

>>>>>>> 04eaf9b8f5daeae71469ba91bcb608fa3cdfaba3
