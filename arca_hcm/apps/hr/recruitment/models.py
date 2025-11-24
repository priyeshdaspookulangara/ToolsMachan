import uuid
from django.db import models
from apps.core.models import BaseModel
from apps.hr.people_core.models import Employee, OrganizationalUnit
from django.contrib.auth.models import User
from .signals import requisition_approved, application_submitted, interview_scheduled, offer_sent, hire_created

class Requisition(BaseModel):
    STATUS_CHOICES = [('DRAFT', 'Draft'), ('OPEN', 'Open'), ('APPROVED', 'Approved'), ('CLOSED', 'Closed'), ('CANCELLED', 'Cancelled')]
    title = models.CharField(max_length=255)
    department = models.ForeignKey(OrganizationalUnit, on_delete=models.PROTECT)
    hiring_manager = models.ForeignKey(Employee, on_delete=models.PROTECT)
    location = models.CharField(max_length=255)
    headcount = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_requisitions')
    approved_at = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=20, blank=True, null=True)
    cost_center = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    approval_workflow = models.JSONField(default=dict)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status == 'APPROVED':
            requisition_approved.send(sender=self.__class__, requisition=self)

class JobPosting(BaseModel):
    requisition = models.ForeignKey(Requisition, on_delete=models.CASCADE)
    external_id = models.CharField(max_length=100, blank=True, null=True)
    board = models.CharField(max_length=100)
    url = models.URLField()
    posted_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20)

class Candidate(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    source = models.CharField(max_length=100)
    resume_file = models.URLField(blank=True, null=True)
    parsed_profile = models.JSONField(default=dict)
    current_title = models.CharField(max_length=255, blank=True, null=True)
    current_company = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

class Application(BaseModel):
    STATUS_CHOICES = [('APPLIED', 'Applied'), ('SCREENING', 'Screening'), ('INTERVIEW', 'Interview'), ('OFFER', 'Offer'), ('HIRED', 'Hired'), ('REJECTED', 'Rejected')]
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    requisition = models.ForeignKey(Requisition, on_delete=models.CASCADE)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='APPLIED')
    applied_at = models.DateTimeField(auto_now_add=True)
    source_ref = models.CharField(max_length=255, blank=True, null=True)
    score = models.FloatField(null=True, blank=True)
    tags = models.JSONField(default=list)
    stage_history = models.JSONField(default=list)

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)
        if is_new:
            application_submitted.send(sender=self.__class__, application=self)

class Interview(BaseModel):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    interviewer = models.ForeignKey(Employee, on_delete=models.PROTECT)
    panel = models.ManyToManyField(Employee, related_name='interview_panels')
    scheduled_start = models.DateTimeField()
    scheduled_end = models.DateTimeField()
    timezone = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    calendar_event_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20)
    feedback = models.JSONField(default=dict)
    score = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status == 'SCHEDULED':
            interview_scheduled.send(sender=self.__class__, interview=self)

class Assessment(BaseModel):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    assessment_type = models.CharField(max_length=100)
    provider_ref = models.CharField(max_length=255, blank=True, null=True)
    score = models.FloatField(null=True, blank=True)
    report_url = models.URLField(blank=True, null=True)
    completed_at = models.DateTimeField(null=True, blank=True)

class Offer(BaseModel):
    STATUS_CHOICES = [('DRAFT', 'Draft'), ('SENT', 'Sent'), ('ACCEPTED', 'Accepted'), ('DECLINED', 'Declined')]
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    offer_template_id = models.CharField(max_length=100)
    salary_offered = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10)
    components = models.JSONField(default=dict)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')
    sent_at = models.DateTimeField(null=True, blank=True)
    accepted_at = models.DateTimeField(null=True, blank=True)
    declined_at = models.DateTimeField(null=True, blank=True)
    approval_chain = models.JSONField(default=list)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status == 'SENT':
            offer_sent.send(sender=self.__class__, offer=self)

class BackgroundCheck(BaseModel):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    provider = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    report = models.JSONField(default=dict)
    completed_at = models.DateTimeField(null=True, blank=True)

class HireRecord(BaseModel):
    STATUS_CHOICES = [('PENDING', 'Pending'), ('IN_PROGRESS', 'In Progress'), ('COMPLETE', 'Complete')]
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    created_employee_id = models.UUIDField(null=True, blank=True)
    onboarding_tasks = models.JSONField(default=list)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)
        if is_new:
            hire_created.send(sender=self.__class__, hire_record=self)
