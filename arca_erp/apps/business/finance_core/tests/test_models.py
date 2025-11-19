from django.test import TestCase
from ..models import ChartOfAccounts, Journal, JournalEntry, Vendor, Customer, AccountsPayable, AccountsReceivable
from django.core.exceptions import ValidationError

class ChartOfAccountsModelTest(TestCase):

    def setUp(self):
        self.asset_account = ChartOfAccounts.objects.create(
            account_name='Cash',
            account_code='1000',
            account_type='ASSET'
        )

    def test_chart_of_accounts_creation(self):
        self.assertEqual(self.asset_account.account_name, 'Cash')
        self.assertEqual(self.asset_account.account_code, '1000')
        self.assertEqual(self.asset_account.account_type, 'ASSET')
        self.assertEqual(str(self.asset_account), '1000 - Cash')

class JournalModelTest(TestCase):

    def setUp(self):
        self.journal = Journal.objects.create(
            journal_date='2024-01-01',
            description='Test Journal',
            document_number='JRNL-001'
        )
        self.account1 = ChartOfAccounts.objects.create(account_name='Cash', account_code='1000', account_type='ASSET')
        self.account2 = ChartOfAccounts.objects.create(account_name='Revenue', account_code='4000', account_type='INCOME')
        JournalEntry.objects.create(journal=self.journal, account=self.account1, amount=100, entry_type='DEBIT')
        JournalEntry.objects.create(journal=self.journal, account=self.account2, amount=100, entry_type='CREDIT')

    def test_journal_creation(self):
        self.assertEqual(self.journal.description, 'Test Journal')
        self.assertEqual(self.journal.status, 'DRAFT')
        self.assertEqual(self.journal.entries.count(), 2)

    def test_journal_validation(self):
        unbalanced_journal = Journal.objects.create(
            journal_date='2024-01-02',
            description='Unbalanced',
            document_number='JRNL-002'
        )
        JournalEntry.objects.create(journal=unbalanced_journal, account=self.account1, amount=100, entry_type='DEBIT')
        JournalEntry.objects.create(journal=unbalanced_journal, account=self.account2, amount=50, entry_type='CREDIT')
        with self.assertRaises(ValidationError):
            unbalanced_journal.clean()

class VendorAndCustomerModelTest(TestCase):

    def test_vendor_creation(self):
        vendor = Vendor.objects.create(name='Test Vendor', email='vendor@test.com')
        self.assertEqual(vendor.name, 'Test Vendor')
        self.assertEqual(str(vendor), 'Test Vendor')

    def test_customer_creation(self):
        customer = Customer.objects.create(name='Test Customer', email='customer@test.com')
        self.assertEqual(customer.name, 'Test Customer')
        self.assertEqual(str(customer), 'Test Customer')

class APAndARModelTest(TestCase):

    def setUp(self):
        self.vendor = Vendor.objects.create(name='Test Vendor', email='vendor@test.com')
        self.customer = Customer.objects.create(name='Test Customer', email='customer@test.com')

    def test_ap_creation(self):
        ap = AccountsPayable.objects.create(
            vendor=self.vendor,
            invoice_number='INV-001',
            invoice_date='2024-01-01',
            due_date='2024-01-31',
            amount=1000
        )
        self.assertEqual(ap.vendor.name, 'Test Vendor')
        self.assertEqual(str(ap), 'AP Invoice INV-001 from Test Vendor')

    def test_ar_creation(self):
        ar = AccountsReceivable.objects.create(
            customer=self.customer,
            invoice_number='INV-002',
            invoice_date='2024-01-01',
            due_date='2024-01-31',
            amount=2000
        )
        self.assertEqual(ar.customer.name, 'Test Customer')
        self.assertEqual(str(ar), 'AR Invoice INV-002 to Test Customer')
