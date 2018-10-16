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

class UserSerializer(serializers.ModelSerializer):
    # author = RequisitionSerializer(many=True, read_only=True)
    class Meta:
        model = models.CustomUser
        fields = ('id', 'username', 'es_tecnico')
        # fields = ('id', 'username', 'es_tecnico', 'author')

class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Token
        fields = ('key', 'user',)

<<<<<<< HEAD

class UserSerializer2(serializers.ModelSerializer):
    author = RequisitionSerializer(many=True, read_only=True)
    class Meta:
        model = models.CustomUser
        fields = ('id','author')
=======
# class UserSerializer2(serializers.ModelSerializer):
#     author = RequisitionSerializer(many=True, read_only=True)
#     class Meta:
#         model = models.CustomUser
#         fields = ('id','author')

>>>>>>> ebd42008aae25fcd4b03bd447819f18eddd09e4f
