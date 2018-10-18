from rest_framework import serializers
from rest_framework.authtoken.models import Token
from . import models

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Module
        fields = ('name', 'system')

class RequisitionSerializer(serializers.ModelSerializer):
    type = serializers.CharField(required=True)
    subject = serializers.CharField(required=True)
    priority = serializers.CharField(required=True)
    date = serializers.DateField(required=True)

    class Meta:
        model = models.Requisition
        fields = ('id',
                  'type',
                  'author',
                  'assignedTechnician',
                  'subject',
                  'details',
                  'priority',
                  'affectedSystem',
                  'module',
                  'date',
                  'attachedFile',
                  'constancy')


class UserSerializer(serializers.ModelSerializer):
    # author = RequisitionSerializer(many=True, read_only=True)
    class Meta:
        model = models.CustomUser
        fields = ('id',
                  'username',
                  'isTechnician')

class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Token
        fields = ('key',
                  'user')

class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.System
        fields = ('name')

class ConstansySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Constancy
        fields = ('description',
                  'attachedFile')

# class UserSerializer2(serializers.ModelSerializer):
#     author = RequisitionSerializer(many=True, read_only=True)
#     class Meta:
#         model = models.CustomUser
#         fields = ('id','author')
