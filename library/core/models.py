from uuid import uuid4

from django.db import models


# Create your models here.
def upload_image_member(instance, filename):
    return f"{instance.id_member}-{filename}"


class Members(models.Model):
    id_member = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    vip = models.IntegerField(default=0)
    nome = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(
        upload_to=upload_image_member, blank=True, null=True)
