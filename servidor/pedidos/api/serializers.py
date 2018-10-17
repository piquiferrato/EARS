from rest_framework import serializers
from rest_framework.authtoken.models import Token
from . import models



class RequisitionSerializer(serializers.ModelSerializer):
    type = serializers.CharField(required=True)
    subject = serializers.CharField(required=True)
    priority = serializers.CharField(required=True)
    affected_system = serializers.CharField(required=True)
    module = serializers.CharField(required=True)
    date = serializers.CharField(required=True)

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


class UserSerializer(serializers.ModelSerializer):
    # author = RequisitionSerializer(many=True, read_only=True)
    class Meta:
        model = models.CustomUser
        fields = ('id','username', 'es_tecnico')

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

# class UserSerializer2(serializers.ModelSerializer):
#     author = RequisitionSerializer(many=True, read_only=True)
#     class Meta:
#         model = models.CustomUser
#         fields = ('id','author')
