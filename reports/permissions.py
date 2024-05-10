from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsReportOwnerOrReadOnly(BasePermission):
    """
    Access to update only to the owner.
    """

    def has_object_permission(self, request, view, obj) -> bool:
        if request.method in SAFE_METHODS or request.user == obj.user:
            return True
        return False
