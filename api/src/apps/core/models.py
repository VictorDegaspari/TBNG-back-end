from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
def upload_image_member(instance, filename):
    return f"{instance.id_member}-{filename}"


class Members(models.Model):
    id_member = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    PLANO_BASICO = "Não"
    PLANO_PREMIUM = "Sim"
    PLANOS = (
        (PLANO_BASICO, "básico"),
        (PLANO_PREMIUM, "premium")
    )
    vip = models.CharField(max_length=3,choices=PLANOS, default="Não")
    nome = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(
        upload_to=upload_image_member, blank=True, null=True)
