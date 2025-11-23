from ..models import AccountsReceivable

class ARService:
    @staticmethod
    def record_invoice(customer, invoice_number, invoice_date, due_date, amount):
        ar = AccountsReceivable.objects.create(
            customer=customer,
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            due_date=due_date,
            amount=amount
        )
        return ar

    @staticmethod
    def mark_as_received(invoice_id):
        ar = AccountsReceivable.objects.get(id=invoice_id)
        ar.received = True
        ar.save()
        return ar
