from rest_framework import viewsets
from ..models import ChartOfAccounts, Journal, AccountsPayable, AccountsReceivable, BankAccount
from .serializers import ChartOfAccountsSerializer, JournalSerializer, AccountsPayableSerializer, AccountsReceivableSerializer, BankAccountSerializer

class ChartOfAccountsViewSet(viewsets.ModelViewSet):
    queryset = ChartOfAccounts.objects.all()
    serializer_class = ChartOfAccountsSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from ..services.posting_engine import PostingEngine

class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

    @action(detail=True, methods=['post'])
    def post_journal(self, request, pk=None):
        journal = self.get_object()
        try:
            PostingEngine.post_journal(journal)
            return Response({'status': 'journal posted'})
        except ValueError as e:
            return Response({'error': str(e)}, status=400)


class AccountsPayableViewSet(viewsets.ModelViewSet):
    queryset = AccountsPayable.objects.all()
    serializer_class = AccountsPayableSerializer


class AccountsReceivableViewSet(viewsets.ModelViewSet):
    queryset = AccountsReceivable.objects.all()
    serializer_class = AccountsReceivableSerializer


class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
