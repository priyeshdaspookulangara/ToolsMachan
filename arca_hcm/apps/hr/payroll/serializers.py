from rest_framework import serializers
from .models import (
    EmployeeSnapshot, PayComponent, PayrollSchedule, PayrollRun,
    PayrollRunResult, PayrollInput, RetroAdjustment, Payslip,
    PayrollJournalEntry, StatutoryRule
)

class EmployeeSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSnapshot
        fields = '__all__'

class PayComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayComponent
        fields = '__all__'

class PayrollScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollSchedule
        fields = '__all__'

class PayrollRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollRun
        fields = '__all__'

class PayrollRunResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollRunResult
        fields = '__all__'

class PayrollInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollInput
        fields = '__all__'

class RetroAdjustmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetroAdjustment
        fields = '__all__'

class PayslipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payslip
        fields = '__all__'

class PayrollJournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollJournalEntry
        fields = '__all__'

class StatutoryRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatutoryRule
        fields = '__all__'
