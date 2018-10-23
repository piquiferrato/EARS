from rest_framework import serializers
from rest_framework.authtoken.models import Token
from . import models

class ModuleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    class Meta:
        model = models.Module
        fields = ('id',
                  'name',
                  'system')

class RequisitionSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(required=True)
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
                  'constancy',
                  'status',)

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
    name = serializers.CharField(required=True)
    class Meta:
        model = models.System
        fields = ('id',
                  'name')

class ConstancySerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=True)
    finishDate = serializers.DateField(required=True)
    class Meta:
        model = models.Constancy
        fields = ('id',
                  'description',
                  'attachedFile',
                  'finishDate')

class RequerimentConstancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Requisition
        fields = ('id',
                  'affectedSystem',
                  'type',
                  'module',
                  'constancy')

class StatusSerializer(serializers.ModelSerializer):
    current = serializers.CharField(required=True)
    class Meta:
        model = models.Status
        fields = ('id',
                  'current')

class PrioritySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    class Meta:
        model = models.Priority
        fields = ('id',
                  'name')

class TypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    class Meta:
        model = models.Type
        fields = ('id',
                  'name')

class AffectedSystemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Requisition
        fields = 'affectedSystem'

class AffectedModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Requisition
        fields = 'module'

class AffectedConstancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Requisition
        fields = 'constancy'
