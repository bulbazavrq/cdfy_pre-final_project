from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from accounts import serializers
from accounts.models import Role
# from accounts.serializers import RoleSerializer

User = get_user_model()


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.CustomUserCreateSerializer
        elif self.action == 'list':
            return serializers.CustomUserListSerializer
        return serializers.CustomUserDetailSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    # serializer_class = serializers.RoleSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.RoleSerializer
        return serializers.RoleSerializer
        # return RoleSerializer
