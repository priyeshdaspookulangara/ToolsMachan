from django.db import models
from apps.core.models import BaseModel
from apps.hr.org_core.models import Department, Position

class Employee(BaseModel):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('On Leave', 'On Leave'),
        ('Terminated', 'Terminated'),
    ]

    employee_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    personal_email = models.EmailField(unique=True, null=True, blank=True)
    work_email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    hire_date = models.DateField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    bank_account = models.JSONField(default=dict)
    address = models.JSONField(default=dict)
    emergency_contact = models.JSONField(default=dict)
    metadata = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.employee_id})"
