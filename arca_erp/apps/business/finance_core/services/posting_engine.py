from django.db import transaction
from ..models import Journal, JournalEntry, Ledger

class PostingEngine:
    @staticmethod
    @transaction.atomic
    def post_journal(journal: Journal):
        if journal.status != 'APPROVED':
            raise ValueError("Journal must be approved before posting.")

        credit_increase_accounts = ['LIABILITY', 'EQUITY', 'INCOME']

        for entry in journal.entries.all():
            ledger, _ = Ledger.objects.get_or_create(account=entry.account)

            if entry.entry_type == 'DEBIT':
                if entry.account.account_type in credit_increase_accounts:
                    ledger.balance -= entry.amount
                else:
                    ledger.balance += entry.amount
            else:  # CREDIT
                if entry.account.account_type in credit_increase_accounts:
                    ledger.balance += entry.amount
                else:
                    ledger.balance -= entry.amount

            ledger.save()

        journal.status = 'POSTED'
        journal.save()
