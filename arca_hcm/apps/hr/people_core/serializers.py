from rest_framework import serializers
from .models import (
    Employee, Employment, OrganizationalUnit, Position,
    AssignmentHistory, CompensationStructureMeta
)

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employment
        fields = '__all__'

class OrganizationalUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationalUnit
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class AssignmentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentHistory
        fields = '__all__'

class CompensationStructureMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompensationStructureMeta
        fields = '__all__'
