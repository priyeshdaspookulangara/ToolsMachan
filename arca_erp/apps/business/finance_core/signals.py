from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.retail.retail_pos.models import Sale
from apps.business.material_core.models import PurchaseOrder

@receiver(post_save, sender=Sale)
def create_journal_from_sale(sender, instance, created, **kwargs):
    if created:
        # Placeholder for creating a journal entry from a POS sale
        print(f"Sale {instance.id} created. Create journal entry.")

@receiver(post_save, sender=PurchaseOrder)
def create_journal_from_po(sender, instance, created, **kwargs):
    if created:
        # Placeholder for creating a journal entry from a purchase order
        print(f"PO {instance.id} created. Create journal entry.")
