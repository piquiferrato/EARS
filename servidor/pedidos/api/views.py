from django.shortcuts import render
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated

# Create your views here.

from . import models
from . import serializers

WAITING = 1
INPROGRESS = 2
CANCELLED = 3
DONE = 4

class UserListView(generics.ListAPIView):
    lookup_field = 'id'
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

class UniqueUserListView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = models.CustomUser.objects
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.CustomUser.objects.filter(id=id)

class RequisitionListView(generics.ListCreateAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer
    queryset = models.Requisition.objects.all()

class DeleteRequisitionView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = models.Requisition.objects.all()
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
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
        id = self.kwargs['id']
        return models.Requisition.objects.filter(author=id)

class SystemsView(generics.ListCreateAPIView):
    lookup_filed = 'id'
    queryset = models.System.objects.all()
    serializer_class = serializers.SystemSerializer

class ModulesView(generics.ListCreateAPIView):
    lookup_filed = 'id'
    queryset = models.Module.objects.all()
    serializer_class = serializers.ModuleSerializer

class ConstancysView(generics.ListCreateAPIView):
    lookup_field = 'id'
    queryset = models.Constancy.objects.all()
    serializer_class = serializers.ConstancySerializer

class UniqueSystemView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = serializers.SystemSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.System.objects.filter(id=id)

class DeleteSystemView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = serializers.SystemSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.System.objects.filter(id=id)

class UniqueModuleView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = serializers.ModuleSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Module.objects.filter(id=id)

class DeleteModuleView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = serializers.ModuleSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Module.objects.filter(id=id)

class UniqueConstancyView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = serializers.ConstancySerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Constancy.objects.filter(id=id)

class DeleteConstancyView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = serializers.ConstancySerializer

    def get_queryset(self):
        id = self.kwargs['id']

        return models.Constancy.objects.filter(id=id)

class SystemModulesView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.ModuleSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Module.objects.all().filter(system=id)

class StatusView(generics.ListCreateAPIView):
    lookup_field = 'id'
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer

class PriorityView(generics.ListCreateAPIView):
    lookup_field = 'id'
    queryset = models.Priority.objects.all()
    serializer_class = serializers.PrioritySerializer

class RequisitionByStatusView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Requisition.objects.all().filter(status=id)

class OrderRequisitionByPriority(generics.ListAPIView):
    lookup_field = 'id'
    queryset = models.Requisition.objects.all().order_by('priority')
    serializer_class = serializers.RequisitionSerializer

class OrderRequisitionByDate(generics.ListAPIView):
    lookup_field = 'id'
    queryset = models.Requisition.objects.all().order_by('date')
    serializer_class = serializers.RequisitionSerializer

class OrderRequisitionByAuthor(generics.ListAPIView):
    lookup_field = 'id'
    queryset = models.Requisition.objects.all().order_by('author')
    serializer_class = serializers.RequisitionSerializer

class Priority(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = models.Requisition.objects.all()
    serializer_class = serializers.PrioritySerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Priority.objects.all().filter(id=id)

class UnderwayByTechnicianView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        underwayId = 2
        return models.Requisition.objects.all().filter(assignedTechnician = id, status = INPROGRESS)

class ImplementedByTechnicianView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        doneId = 4
        return models.Requisition.objects.all().filter(assignedTechnician = id, status = DONE)

# class FinishedModulesBySystem(generics.ListAPIView):
#     lookup_field = 'id'
#     serializer_class = serializers.RequerimentConstancySerializer
#
#     def get_queryset(self):
#         systemId = self.kwargs['system']
#         return models.Requisition.objects.all().filter(affectedSystem = systemId, status = DONE)

class TypesView(generics.ListCreateAPIView):
    lookup_filed = 'id'
    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer

class AffectedSystems(generics.ListAPIView):
    lookup_filed = 'id'
    queryset = models.Requisition.objects.all().filter(status = DONE)
    serializer_class = serializers.AffectedSystemsSerializer

class SystemAffectedModules(generics.ListAPIView):
    lookup_filed = 'id'
    serializer_class = serializers.AffectedModulesSerializer

    def get_queryset(self):
        systemId = self.kwargs['system']
        return models.Requisition.objects.all().filter(affectedSystem = systemId, status = DONE)

class ModulesConstancy(generics.ListAPIView):
    lookup_filed = 'id'
    serializer_class = serializers.AffectedConstancySerializer

    def get_queryset(self):
        moduleId = self.kwargs['module']
        return models.Requisition.objects.all().filter(module = moduleId, status = DONE)

