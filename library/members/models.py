from uuid import uuid4

from django.db import models

# Create your models here.


class Members(models.Model):
    id_members = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    vip = models.IntegerField(default=0)
    nickname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    max_mmr = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
