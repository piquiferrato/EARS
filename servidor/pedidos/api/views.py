from django.shortcuts import render
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

from . import models
from . import serializers

class UserListView(generics.ListAPIView):
    lookup_field = 'id'
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

class UniqueUserListView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = models.CustomUser.objects
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        id = self.kwargs['id']
        return models.CustomUser.objects.filter(id=id)

class RequisitionListView(generics.ListCreateAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer
    queryset = models.Requisition.objects.all()

class ErrorsListView(generics.ListAPIView):
    queryset = models.Requisition.objects.filter(type='error')
    serializer_class = serializers.UserSerializer

class DeleteRequisitionView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = models.Requisition.objects.all()
    serializer_class = serializers.RequisitionSerializer


    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        id = self.kwargs['id']
        return models.Requisition.objects.filter(id=id)

class UpdateRequisitionView(generics.UpdateAPIView):
    lookup_field = 'id'
    queryset = models.Requisition.objects.all()
    serializer_class = serializers.RequisitionSerializer

class MyRequisitionsListView(generics.ListAPIView):
    lookup_field = 'id'
    queryset = models.Requisition.objects
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        id = self.kwargs['id']
        return models.Requisition.objects.filter(author=id)

# class MyRequisitionsListView(generics.ListAPIView):
#     lookup_field = 'slug'
#     lookup_url_kwarg = 'id'
#     # queryset = models.Requisition.objects
#     serializer_class = serializers.RequisitionSerializer
#
#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases for
#         the user as determined by the username portion of the URL.
#         """
#         id = self.kwargs['id']
#         return models.Requisition.objects.all().filter(author=id)


        def get_queryset(self):
            """
            This view should return a list of all the purchases for
            the user as determined by the username portion of the URL.
            """
            id = self.kwargs['id']
            return models.CustomUser.objects.filter(id=id)

class MyRequisitionsListView(generics.ListAPIView):
    lookup_field = 'id'
    queryset = models.Requisition.objects
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        id = self.kwargs['id']
        return models.Requisition.objects.filter(author=id)

# class MyRequisitionsListView(generics.ListAPIView):
#     lookup_field = 'slug'
#     lookup_url_kwarg = 'id'
#     queryset = models.Requisition.objects
#     serializer_class = serializers.RequisitionSerializer
#
#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases for
#         the user as determined by the username portion of the URL.
#         """
#         id = self.kwargs['id']
#         return models.Requisition.objects.filter(author=id)
