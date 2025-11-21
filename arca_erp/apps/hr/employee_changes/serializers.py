from rest_framework import serializers
from .models import EmployeeChangeRequest, EmployeeApproval, ApprovalRule

class EmployeeChangeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeChangeRequest
        fields = '__all__'
        read_only_fields = ('requested_by', 'status', 'applied_at', 'rejection_reason', 'payload_before')

class EmployeeApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeApproval
        fields = '__all__'
        read_only_fields = ('approver',)

class ApprovalRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalRule
        fields = '__all__'
