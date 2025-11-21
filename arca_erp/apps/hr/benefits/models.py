from django.db import models
from apps.core.models import BaseModel
from apps.hr.people_core.models import Employee

class BenefitPlan(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    provider = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class BenefitEnrollment(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    plan = models.ForeignKey(BenefitPlan, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.employee} enrolled in {self.plan}"
