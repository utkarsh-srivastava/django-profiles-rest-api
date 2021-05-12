from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to edit own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """allow users to udpate their owns status"""

    def has_object_permission(self, request, view, obj):
        """check the user is trying to udpate their own status"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
