from rest_framework import serializers
from ..models import ChartOfAccounts, Journal, JournalEntry, AccountsPayable, AccountsReceivable, BankAccount

class ChartOfAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartOfAccounts
        fields = '__all__'

class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = ['account', 'amount', 'entry_type', 'cost_center']

class JournalSerializer(serializers.ModelSerializer):
    entries = JournalEntrySerializer(many=True)

    class Meta:
        model = Journal
        fields = ['journal_date', 'description', 'status', 'entries']

    def validate(self, data):
        debits = sum(entry['amount'] for entry in data['entries'] if entry['entry_type'] == 'DEBIT')
        credits = sum(entry['amount'] for entry in data['entries'] if entry['entry_type'] == 'CREDIT')

        if debits != credits:
            raise serializers.ValidationError("Debits and credits must be equal.")

        return data

    def create(self, validated_data):
        entries_data = validated_data.pop('entries')
        journal = Journal.objects.create(**validated_data)
        for entry_data in entries_data:
            JournalEntry.objects.create(journal=journal, **entry_data)
        return journal


class AccountsPayableSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsPayable
        fields = '__all__'


class AccountsReceivableSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsReceivable
        fields = '__all__'


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'
