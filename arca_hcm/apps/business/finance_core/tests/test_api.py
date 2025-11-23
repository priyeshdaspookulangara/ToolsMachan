from rest_framework.test import APITestCase
from rest_framework import status
from ..models import ChartOfAccounts
from django.contrib.auth import get_user_model

User = get_user_model()

class ChartOfAccountsAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.account_data = {'account_name': 'Cash', 'account_code': '1000', 'account_type': 'ASSET'}
        self.account = ChartOfAccounts.objects.create(**self.account_data)
        self.url = '/api/finance_core/api/chart-of-accounts/'

    def test_get_chart_of_accounts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_chart_of_accounts(self):
        new_account_data = {'account_name': 'Bank', 'account_code': '1010', 'account_type': 'ASSET'}
        response = self.client.post(self.url, new_account_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreaterEqual(ChartOfAccounts.objects.count(), 2)

from ..models import Journal, JournalEntry

class JournalAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.account1 = ChartOfAccounts.objects.create(account_name='Cash', account_code='1000', account_type='ASSET')
        self.account2 = ChartOfAccounts.objects.create(account_name='Revenue', account_code='4000', account_type='INCOME')

    def test_post_journal_action(self):
        journal = Journal.objects.create(
            journal_date='2024-01-01',
            description='Test Journal',
            document_number='JRNL-001',
            status='APPROVED'
        )
        JournalEntry.objects.create(journal=journal, account=self.account1, amount=100, entry_type='DEBIT')
        JournalEntry.objects.create(journal=journal, account=self.account2, amount=100, entry_type='CREDIT')

        url = f'/api/finance_core/api/journals/{journal.id}/post_journal/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        journal.refresh_from_db()
        self.assertEqual(journal.status, 'POSTED')
