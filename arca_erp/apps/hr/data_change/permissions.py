from rest_framework.permissions import BasePermission
from apps.hr.people_core.models import Employee

class IsHRAuditOrAdmin(BasePermission):
    """
    Allows access only to HR Auditors (read-only) or HR Admins (full access).
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if view.action in ['list', 'retrieve']:
            return request.user.groups.filter(name__in=['HR Audit', 'HR Admin']).exists()
        return request.user.groups.filter(name='HR Admin').exists()

class CanRequestChange(BasePermission):
    """
    Allows employees to request changes for themselves.
    """
    def has_object_permission(self, request, view, obj):
        return obj.work_email == request.user.email

class CanApproveChange(BasePermission):
    """
    Allows authorized users to approve changes based on rules.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
