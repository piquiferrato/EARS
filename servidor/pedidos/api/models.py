from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    es_tecnico = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Requisition(models.Model):
    type = models.TextField()
    author = models.ForeignKey(CustomUser, related_name = 'author', on_delete=models.CASCADE, null=True)
    assigned_technician = models.ForeignKey(CustomUser, related_name = 'assigned_technician', on_delete=models.CASCADE, null=True)
    subject = models.TextField() #Asunto
    details = models.TextField()
    priority = models.TextField()
    affected_system = models.TextField()
    module = models.TextField()
    date = models.TextField(null=True)
    attached_file = models.FileField(null=True)

    def __str__(self):
        return self.subject