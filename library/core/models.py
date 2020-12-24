import uuid

from django.db import models

# Create your models here.


class Members(models.Model):
    id_member = models.UUIDField(
        primary_key=True, default=uuid, editable=False)
    vip = models.IntegerField()
    nome = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
