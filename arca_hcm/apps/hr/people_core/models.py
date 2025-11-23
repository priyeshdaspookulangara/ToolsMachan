import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .signals import employee_created, employee_updated, employment_changed, employee_terminated, org_changed

class Employee(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
        ('TERMINATED', 'Terminated'),
        ('ON_LEAVE', 'On Leave'),
    ]

    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    email_personal = models.EmailField(unique=True, null=True, blank=True)
    email_official = models.EmailField(unique=True, null=True, blank=True)
    phone_personal = models.CharField(max_length=20, blank=True, null=True)
    phone_official = models.CharField(max_length=20, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    marital_status = models.CharField(max_length=20, blank=True, null=True)
    blood_group = models.CharField(max_length=10, blank=True, null=True)
    identifications = models.JSONField(default=dict)
    photo_url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    date_joined = models.DateField()
    date_confirmed = models.DateField(blank=True, null=True)
    date_terminated = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)
        if is_new:
            employee_created.send(sender=self.__class__, employee=self)
        else:
            employee_updated.send(sender=self.__class__, employee=self)
        if self.status == 'TERMINATED':
            employee_terminated.send(sender=self.__class__, employee=self)

class OrganizationalUnit(models.Model):
    org_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    type = models.CharField(max_length=100)
    head = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='led_units')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    metadata = models.JSONField(default=dict)

    def __str__(self):
        return self.name

    def clean(self):
        if self.parent == self:
            raise ValidationError("An organizational unit cannot be its own parent.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        org_changed.send(sender=self.__class__, org_unit=self)

class Position(models.Model):
    position_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    job_code = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    department = models.ForeignKey(OrganizationalUnit, on_delete=models.PROTECT)
    reports_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    vacancy_status = models.CharField(max_length=50)
    metadata = models.JSONField(default=dict)

    def __str__(self):
        return self.title

class Employment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    job_code = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    employee_type = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=100)
    probation_end_date = models.DateField(blank=True, null=True)
    work_location = models.CharField(max_length=255)
    work_country = models.CharField(max_length=100)
    remote_status = models.CharField(max_length=50)
    effective_from = models.DateField()
    effective_to = models.DateField(blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    department = models.ForeignKey(OrganizationalUnit, on_delete=models.PROTECT)
    cost_center = models.CharField(max_length=100)
    supervisor = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='supervisees')
    is_primary = models.BooleanField(default=True)
    metadata = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.employee} - {self.job_title}"

    def clean(self):
        if self.supervisor == self.employee:
            raise ValidationError("An employee cannot be their own supervisor.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        employment_changed.send(sender=self.__class__, employment=self)

class AssignmentHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    effective_from = models.DateField()
    effective_to = models.DateField(blank=True, null=True)
    action_type = models.CharField(max_length=100)
    remarks = models.TextField(blank=True, null=True)
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    payload_before = models.JSONField()
    payload_after = models.JSONField()

class CompensationStructureMeta(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    structure_code = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    ctc_band = models.CharField(max_length=100)
    currency = models.CharField(max_length=10)
    effective_from = models.DateField()
    effective_to = models.DateField(blank=True, null=True)
    metadata = models.JSONField(default=dict)
