from rest_framework.permissions import BasePermission

class IsManagerOnly(BasePermission):
    """Allow only managers"""
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name="Manager").exists()
        )


class IsDeliveryCrewOnly(BasePermission):
    """Allow delivery crew and managers"""
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and (
                request.user.groups.filter(name="Delivery Crew").exists()
                or request.user.groups.filter(name="Manager").exists()
            )
        )


class IsOwnerOrManager(BasePermission):
    """Allow object owners, or managers full access"""
    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Manager").exists():
            return True
        return obj.user == request.user
