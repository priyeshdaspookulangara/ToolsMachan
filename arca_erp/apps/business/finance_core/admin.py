from django.contrib import admin
from .models import (
    ChartOfAccounts,
    Ledger,
    Journal,
    JournalEntry,
    CostCenter,
    BankAccount,
    Budget,
    Vendor,
    Customer,
    AccountsPayable,
    AccountsReceivable,
)

admin.site.register(ChartOfAccounts)
admin.site.register(Ledger)
admin.site.register(Journal)
admin.site.register(JournalEntry)
admin.site.register(CostCenter)
admin.site.register(BankAccount)
admin.site.register(Budget)
admin.site.register(Vendor)
admin.site.register(Customer)
admin.site.register(AccountsPayable)
admin.site.register(AccountsReceivable)
