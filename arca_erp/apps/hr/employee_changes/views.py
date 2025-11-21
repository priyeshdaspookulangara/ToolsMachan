from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import EmployeeChangeRequest
from .serializers import EmployeeChangeRequestSerializer
from .services.change_request_service import ChangeRequestService
from .services.approval_service import ApprovalService
from .services.apply_change_service import ApplyChangeService
from .permissions import IsHRAuditOrAdmin, CanRequestChange, CanApproveChange

class EmployeeChangeRequestViewSet(viewsets.ModelViewSet):
    queryset = EmployeeChangeRequest.objects.all()
    serializer_class = EmployeeChangeRequestSerializer
    permission_classes = [IsAuthenticated] # Base permission

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, CanRequestChange]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated, IsHRAuditOrAdmin]
        elif self.action in ['approve', 'reject', 'apply']:
            self.permission_classes = [IsAuthenticated, CanApproveChange]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = serializer.validated_data['employee']
        self.check_object_permissions(self.request, obj=employee)
        change_request = ChangeRequestService.create_change_request(
            employee=employee,
            requested_by=self.request.user,
            change_type=serializer.validated_data['change_type'],
            payload_after=serializer.validated_data['payload_after']
        )
        response_serializer = self.get_serializer(change_request)
        headers = self.get_success_headers(response_serializer.data)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['patch'])
    def approve(self, request, pk=None):
        change_request = self.get_object()
        level = request.data.get('level', 1)
        ApprovalService.approve_change_request(change_request, request.user, level)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['patch'])
    def reject(self, request, pk=None):
        change_request = self.get_object()
        level = request.data.get('level', 1)
        reason = request.data.get('reason', '')
        ApprovalService.reject_change_request(change_request, request.user, level, reason)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['patch'])
    def apply(self, request, pk=None):
        change_request = self.get_object()
        ApplyChangeService.apply_change(change_request)
        return Response(status=status.HTTP_200_OK)
