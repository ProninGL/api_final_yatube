from rest_framework import permissions, status


class IsAuthorOrReadOnly(permissions.BasePermission):

    message = "У вас нет прав вносить изменения."
    code = status.HTTP_403_FORBIDDEN

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
