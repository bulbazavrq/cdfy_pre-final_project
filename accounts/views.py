from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from accounts import serializers


User = get_user_model()


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.CustomUserCreateSerializer
        elif self.action == 'list':
            return serializers.CustomUserListSerializer
        return serializers.CustomUserDetailSerializer

