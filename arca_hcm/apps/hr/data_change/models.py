from django.db import models
from django.contrib.auth.models import User
from apps.core.models import BaseModel
from apps.hr.people_core.models import Employee

class EmployeeChangeRequest(BaseModel):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Applied', 'Applied'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    change_type = models.CharField(max_length=255)
    payload_before = models.JSONField()
    payload_after = models.JSONField()
    requested_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='change_requests_made')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    requested_at = models.DateTimeField(auto_now_add=True)
    applied_at = models.DateTimeField(null=True, blank=True)
    rejection_reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Change request for {self.employee} ({self.change_type}) - {self.status}"

class EmployeeApproval(BaseModel):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    change_request = models.ForeignKey(EmployeeChangeRequest, on_delete=models.CASCADE, related_name='approvals')
    approver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    level = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    comment = models.TextField(blank=True, null=True)
    approved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('change_request', 'level')

    def __str__(self):
        return f"Approval for {self.change_request} by {self.approver} (Level {self.level}) - {self.status}"

class ApprovalRule(BaseModel):
    change_type = models.CharField(max_length=255, unique=True)
    levels = models.PositiveSmallIntegerField()
    approver_roles = models.JSONField(default=list)
    conditions = models.JSONField(default=dict)

    def __str__(self):
        return f"Approval rule for {self.change_type} ({self.levels} levels)"

class EmployeeHistorySnapshot(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='history')
    snapshot = models.JSONField()
    changed_at = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=255)
    reference_change_request = models.ForeignKey(EmployeeChangeRequest, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"History snapshot for {self.employee} at {self.changed_at}"
