# from rest_framework import permissions
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
#
#
# class FirstLvlAccess(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_active()
#
#
# class SecondLvlAccess(FirstLvlAccess):
#     def has_permission(self, request, view):
#         permission = super().has_permission()
#         return all([permission, IsAuthenticated()])
#
#
# class ThirdLvlAccess(SecondLvlAccess):
#     def has_permission(self, request, view):
#         permission = super().has_permission()
#         return all([permission, request.user.is_staff()])
#
# class FourthLvlAccess(ThirdLvlAccess):
#     def has_permission(self, request, view):
#         permission = super().has_permission()
#         return all([permission, IsAdminUser()])
