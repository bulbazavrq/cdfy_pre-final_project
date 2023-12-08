from django.contrib import admin

from roles.models import Role


# Register your models here.
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass
