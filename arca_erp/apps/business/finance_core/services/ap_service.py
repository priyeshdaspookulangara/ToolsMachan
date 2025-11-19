from ..models import AccountsPayable

class APService:
    @staticmethod
    def record_invoice(vendor, invoice_number, invoice_date, due_date, amount):
        ap = AccountsPayable.objects.create(
            vendor=vendor,
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            due_date=due_date,
            amount=amount
        )
        return ap

    @staticmethod
    def mark_as_paid(invoice_id):
        ap = AccountsPayable.objects.get(id=invoice_id)
        ap.paid = True
        ap.save()
        return ap
