from django.db import models
from apps.core.models import BaseModel

class Transaction(BaseModel):
    transaction_id = models.CharField(max_length=100, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Transaction {self.transaction_id} - {self.total_amount}"
