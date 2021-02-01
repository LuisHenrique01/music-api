from rest_framework import permissions

class UsuarioPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj is request.user