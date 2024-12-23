from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUser(BasePermission):

    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
    def has_object_permission(self, request, view, obj):
        return bool( request.method in SAFE_METHODS or request.user == obj.user)