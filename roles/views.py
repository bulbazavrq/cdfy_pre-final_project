from django.shortcuts import render
from rest_framework import viewsets

from roles import serializers
from roles.models import Role


# Create your views here.
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = serializers.RoleSerializer
