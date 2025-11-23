from django.test import TestCase
from ..models import ChartOfAccounts, Journal, JournalEntry, Ledger
from ..services.posting_engine import PostingEngine

class PostingEngineTest(TestCase):

    def setUp(self):
        self.asset_account = ChartOfAccounts.objects.create(account_name='Cash', account_code='1000', account_type='ASSET')
        self.liability_account = ChartOfAccounts.objects.create(account_name='Accounts Payable', account_code='2000', account_type='LIABILITY')
        self.income_account = ChartOfAccounts.objects.create(account_name='Revenue', account_code='4000', account_type='INCOME')

    def test_debit_to_asset(self):
        journal = Journal.objects.create(journal_date='2024-01-01', description='Debit Asset', document_number='JRNL-001', status='APPROVED')
        JournalEntry.objects.create(journal=journal, account=self.asset_account, amount=100, entry_type='DEBIT')
        JournalEntry.objects.create(journal=journal, account=self.income_account, amount=100, entry_type='CREDIT')
        PostingEngine.post_journal(journal)
        ledger = Ledger.objects.get(account=self.asset_account)
        self.assertEqual(ledger.balance, 100)

    def test_credit_to_liability(self):
        journal = Journal.objects.create(journal_date='2024-01-01', description='Credit Liability', document_number='JRNL-002', status='APPROVED')
        JournalEntry.objects.create(journal=journal, account=self.asset_account, amount=100, entry_type='DEBIT')
        JournalEntry.objects.create(journal=journal, account=self.liability_account, amount=100, entry_type='CREDIT')
        PostingEngine.post_journal(journal)
        ledger = Ledger.objects.get(account=self.liability_account)
        self.assertEqual(ledger.balance, 100)

    def test_credit_to_income(self):
        journal = Journal.objects.create(journal_date='2024-01-01', description='Credit Income', document_number='JRNL-003', status='APPROVED')
        JournalEntry.objects.create(journal=journal, account=self.asset_account, amount=100, entry_type='DEBIT')
        JournalEntry.objects.create(journal=journal, account=self.income_account, amount=100, entry_type='CREDIT')
        PostingEngine.post_journal(journal)
        ledger = Ledger.objects.get(account=self.income_account)
        self.assertEqual(ledger.balance, 100)
