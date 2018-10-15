from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    es_tecnico = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Requisition(models.Model):
    type = models.TextField(blank=True, null=True)
    author = models.ForeignKey(CustomUser, related_name = 'author', on_delete=models.CASCADE, blank=True, null=True)
    assigned_technician = models.ForeignKey(CustomUser, related_name = 'assigned_technician', blank=True, on_delete=models.CASCADE, null=True)
    subject = models.TextField(blank=True, null=True) #Asunto
    details = models.TextField(blank=True, null=True)
    priority = models.TextField(blank=True, null=True)
    affected_system = models.TextField(blank=True, null=True)
    module = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    attached_file = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.subject