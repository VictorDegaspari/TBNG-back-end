import csv
import random
from datetime import date

import django_filters.rest_framework
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import (BaseFilterBackend, OrderingFilter,
                                    SearchFilter)
from rest_framework.generics import (GenericAPIView, ListAPIView,
                                     ListCreateAPIView)
from rest_framework.pagination import (LimitOffsetPagination,
                                       PageNumberPagination)
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework_csv.renderers import CSVRenderer

from .models import *
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer
