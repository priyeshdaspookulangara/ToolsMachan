from ..models import EmployeeChangeRequest, EmployeeHistorySnapshot
from ..signals import employee_data_changed
from django.utils import timezone

class ApplyChangeService:
    @staticmethod
    def apply_change(change_request):
        """
        Applies the changes from an approved request to the employee model.
        """
        if change_request.status != 'Approved':
            raise ValueError("Change request is not approved.")

        employee = change_request.employee
        for field, value in change_request.payload_after.items():
            setattr(employee, field, value)
        employee.save()

        change_request.status = 'Applied'
        change_request.applied_at = timezone.now()
        change_request.save()

        EmployeeHistorySnapshot.objects.create(
            employee=employee,
            snapshot=change_request.payload_after,
            reason=f"Applied change request: {change_request.change_type}",
            reference_change_request=change_request,
        )

        employee_data_changed.send(sender=__class__, employee=employee, change_request=change_request)

        return employee
