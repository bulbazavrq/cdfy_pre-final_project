from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.CustomUserViewSet)
router.register(r'role', views.RoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
