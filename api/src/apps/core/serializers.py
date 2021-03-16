from django.contrib.auth.models import Group, User
from django.db.models import Q
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['vip', 'nickname', 'nome', 'created_at']
