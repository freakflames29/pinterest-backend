from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        data =  bool(request.user == obj.user)
        print("*"*100,data)
        return data