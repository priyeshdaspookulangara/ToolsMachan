from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    Employee, Employment, OrganizationalUnit, Position,
    AssignmentHistory, CompensationStructureMeta
)
from .serializers import (
    EmployeeSerializer, EmploymentSerializer, OrganizationalUnitSerializer,
    PositionSerializer, AssignmentHistorySerializer, CompensationStructureMetaSerializer
)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmploymentViewSet(viewsets.ModelViewSet):
    queryset = Employment.objects.all()
    serializer_class = EmploymentSerializer

class OrganizationalUnitViewSet(viewsets.ModelViewSet):
    queryset = OrganizationalUnit.objects.all()
    serializer_class = OrganizationalUnitSerializer

    @action(detail=False, methods=['get'])
    def tree(self, request):
        """
        Returns the organizational structure as a nested tree.
        """
        roots = OrganizationalUnit.objects.filter(parent__isnull=True)
        data = []
        for root in roots:
            data.append(self._get_node_data(root))
        return Response(data)

    def _get_node_data(self, node):
        return {
            'id': node.org_id,
            'name': node.name,
            'children': [self._get_node_data(child) for child in node.organizationalunit_set.all()]
        }

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class AssignmentHistoryViewSet(viewsets.ModelViewSet):
    queryset = AssignmentHistory.objects.all()
    serializer_class = AssignmentHistorySerializer

class CompensationStructureMetaViewSet(viewsets.ModelViewSet):
    queryset = CompensationStructureMeta.objects.all()
    serializer_class = CompensationStructureMetaSerializer
