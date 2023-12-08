from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser, Role

User = get_user_model()

# Register your models here.
# admin.site.register(Role)
# admin.site.register(CustomUser, UserAdmin)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass
