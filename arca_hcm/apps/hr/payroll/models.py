from django.db import models
from apps.core.models import BaseModel
from apps.hr.people_core.models import Employee
from django.contrib.auth.models import User

class EmployeeSnapshot(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    payroll_run = models.ForeignKey('PayrollRun', on_delete=models.CASCADE)
    data = models.JSONField()

class PayComponent(BaseModel):
    COMPONENT_TYPES = [('Earning', 'Earning'), ('Deduction', 'Deduction')]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=COMPONENT_TYPES)
    is_taxable = models.BooleanField(default=True)
    is_proratable = models.BooleanField(default=True)
    priority = models.IntegerField(default=100)
    formula = models.TextField(blank=True, null=True)

class PayrollSchedule(BaseModel):
    name = models.CharField(max_length=100)
    frequency = models.CharField(max_length=50) # Monthly, Weekly, etc.

class PayrollRun(BaseModel):
    STATUS_CHOICES = [('Queued', 'Queued'), ('Running', 'Running'), ('Completed', 'Completed'), ('Failed', 'Failed')]
    schedule = models.ForeignKey(PayrollSchedule, on_delete=models.PROTECT)
    period_start = models.DateField()
    period_end = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Queued')
    initiated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class PayrollRunResult(BaseModel):
    payroll_run = models.ForeignKey(PayrollRun, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    gross_earnings = models.DecimalField(max_digits=12, decimal_places=2)
    net_pay = models.DecimalField(max_digits=12, decimal_places=2)
    component_breakdown = models.JSONField()

class PayrollInput(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    payroll_run = models.ForeignKey(PayrollRun, on_delete=models.CASCADE)
    component = models.ForeignKey(PayComponent, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)

class RetroAdjustment(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    effective_date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    reason = models.TextField()

class Payslip(BaseModel):
    payroll_run_result = models.OneToOneField(PayrollRunResult, on_delete=models.CASCADE)
    data = models.JSONField()
    pdf_path = models.CharField(max_length=255, blank=True, null=True)

class PayrollJournalEntry(BaseModel):
    payroll_run = models.ForeignKey(PayrollRun, on_delete=models.CASCADE)
    payload = models.JSONField()
    is_posted = models.BooleanField(default=False)

class StatutoryRule(BaseModel):
    name = models.CharField(max_length=100)
    rule_definition = models.JSONField()
    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)
