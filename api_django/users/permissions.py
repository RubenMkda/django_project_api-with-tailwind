from rest_framework.permissions import IsAuthenticated

class IsAuthenticatedOrCreateOnly(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return super().has_permission(request, view)