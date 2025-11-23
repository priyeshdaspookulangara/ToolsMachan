from django.db import models
from django.conf import settings
from apps.core.models import BaseModel
from decimal import Decimal

class ChartOfAccounts(BaseModel):
    ACCOUNT_TYPES = [
        ('ASSET', 'Asset'),
        ('LIABILITY', 'Liability'),
        ('EQUITY', 'Equity'),
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    ]

    account_name = models.CharField(max_length=255)
    account_code = models.CharField(max_length=50, unique=True)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    parent_account = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    level = models.PositiveIntegerField(default=1)
    is_reconciliation_account = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.account_code} - {self.account_name}"

class Ledger(BaseModel):
    account = models.ForeignKey(ChartOfAccounts, on_delete=models.PROTECT)
    balance = models.DecimalField(max_digits=18, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"Ledger for {self.account.account_name}"

class Journal(BaseModel):
    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('SUBMITTED', 'Submitted'),
        ('APPROVED', 'Approved'),
        ('POSTED', 'Posted'),
    ]

    journal_date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DRAFT')
    document_number = models.CharField(max_length=255, unique=True, editable=False)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='posted_journals')
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='approved_journals')

    def __str__(self):
        return f"Journal {self.document_number} - {self.status}"

    def clean(self):
        from django.core.exceptions import ValidationError

        debits = sum(entry.amount for entry in self.entries.all() if entry.entry_type == 'DEBIT')
        credits = sum(entry.amount for entry in self.entries.all() if entry.entry_type == 'CREDIT')

        if debits != credits:
            raise ValidationError("Debits and credits must be equal.")

class JournalEntry(BaseModel):
    ENTRY_TYPES = [
        ('DEBIT', 'Debit'),
        ('CREDIT', 'Credit'),
    ]

    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name='entries')
    account = models.ForeignKey(ChartOfAccounts, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    entry_type = models.CharField(max_length=6, choices=ENTRY_TYPES)
    cost_center = models.ForeignKey('CostCenter', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.entry_type} of {self.amount} to {self.account.account_name}"

class CostCenter(BaseModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class BankAccount(BaseModel):
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50, unique=True)
    account_holder_name = models.CharField(max_length=255)
    gl_account = models.OneToOneField(ChartOfAccounts, on_delete=models.PROTECT, related_name='bank_account')
    last_reconciliation_date = models.DateField(null=True, blank=True)
    current_balance_from_statement = models.DecimalField(max_digits=18, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"{self.bank_name} - {self.account_number}"

class Budget(BaseModel):
    budget_name = models.CharField(max_length=255)
    fiscal_year = models.PositiveIntegerField()
    account = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    cost_center = models.ForeignKey(CostCenter, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Budget for {self.account.account_name} in {self.fiscal_year}"


class AccountsPayable(BaseModel):
    vendor = models.ForeignKey('Vendor', on_delete=models.PROTECT, related_name='ap_invoices')
    invoice_number = models.CharField(max_length=255)
    invoice_date = models.DateField()
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"AP Invoice {self.invoice_number} from {self.vendor.name}"


class AccountsReceivable(BaseModel):
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT, related_name='ar_invoices')
    invoice_number = models.CharField(max_length=255)
    invoice_date = models.DateField()
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    received = models.BooleanField(default=False)

    def __str__(self):
        return f"AR Invoice {self.invoice_number} to {self.customer.name}"

class Vendor(BaseModel):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Customer(BaseModel):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
