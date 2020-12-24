from django.db import IntegrityError, transaction
from rest_framework import viewsets
from rest_framework.views import APIView

from .models import *
from .serializers import *

# Create your views here.


class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer
