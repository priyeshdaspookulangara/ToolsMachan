from rest_framework import viewsets
from .models import (
    EmployeeSnapshot, PayComponent, PayrollSchedule, PayrollRun,
    PayrollRunResult, PayrollInput, RetroAdjustment, Payslip,
    PayrollJournalEntry, StatutoryRule
)
from .serializers import (
    EmployeeSnapshotSerializer, PayComponentSerializer, PayrollScheduleSerializer,
    PayrollRunSerializer, PayrollRunResultSerializer, PayrollInputSerializer,
    RetroAdjustmentSerializer, PayslipSerializer, PayrollJournalEntrySerializer,
    StatutoryRuleSerializer
)

class EmployeeSnapshotViewSet(viewsets.ModelViewSet):
    queryset = EmployeeSnapshot.objects.all()
    serializer_class = EmployeeSnapshotSerializer

class PayComponentViewSet(viewsets.ModelViewSet):
    queryset = PayComponent.objects.all()
    serializer_class = PayComponentSerializer

class PayrollScheduleViewSet(viewsets.ModelViewSet):
    queryset = PayrollSchedule.objects.all()
    serializer_class = PayrollScheduleSerializer

class PayrollRunViewSet(viewsets.ModelViewSet):
    queryset = PayrollRun.objects.all()
    serializer_class = PayrollRunSerializer

class PayrollRunResultViewSet(viewsets.ModelViewSet):
    queryset = PayrollRunResult.objects.all()
    serializer_class = PayrollRunResultSerializer

class PayrollInputViewSet(viewsets.ModelViewSet):
    queryset = PayrollInput.objects.all()
    serializer_class = PayrollInputSerializer

class RetroAdjustmentViewSet(viewsets.ModelViewSet):
    queryset = RetroAdjustment.objects.all()
    serializer_class = RetroAdjustmentSerializer

class PayslipViewSet(viewsets.ModelViewSet):
    queryset = Payslip.objects.all()
    serializer_class = PayslipSerializer

class PayrollJournalEntryViewSet(viewsets.ModelViewSet):
    queryset = PayrollJournalEntry.objects.all()
    serializer_class = PayrollJournalEntrySerializer

class StatutoryRuleViewSet(viewsets.ModelViewSet):
    queryset = StatutoryRule.objects.all()
    serializer_class = StatutoryRuleSerializer
