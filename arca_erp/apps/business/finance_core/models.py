from django.db import models
from apps.core.models import BaseModel

class JournalEntry(BaseModel):
    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    account = models.CharField(max_length=100) # Simplified for example

    def __str__(self):
        return f"Journal Entry for {self.account} on {self.date}"
