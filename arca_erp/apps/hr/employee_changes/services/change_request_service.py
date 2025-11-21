from ..models import EmployeeChangeRequest, ApprovalRule
from ..signals import employee_change_requested
from django.core.exceptions import ValidationError
from apps.hr.people_ops.serializers import EmployeeSerializer

class ChangeRequestService:
    # In a real application, this would be more dynamic (e.g., stored in the database)
    ALLOWED_CHANGE_TYPES = {
        'personal_info': ['first_name', 'last_name', 'personal_email'],
        'address': ['address'],
        'bank_details': ['bank_account'],
    }

    @staticmethod
    def _validate_payload(change_type, payload):
        if change_type not in ChangeRequestService.ALLOWED_CHANGE_TYPES:
            raise ValidationError(f"Invalid change type: {change_type}")

        required_fields = ChangeRequestService.ALLOWED_CHANGE_TYPES[change_type]
        for field in required_fields:
            if field not in payload:
                raise ValidationError(f"Missing required field '{field}' for change type '{change_type}'")

    @staticmethod
    def create_change_request(employee, requested_by, change_type, payload_after):
        """
        Creates a new employee change request.
        """
        ChangeRequestService._validate_payload(change_type, payload_after)

        payload_before = EmployeeSerializer(employee).data
        change_request = EmployeeChangeRequest.objects.create(
            employee=employee,
            requested_by=requested_by,
            change_type=change_type,
            payload_before=payload_before,
            payload_after=payload_after,
        )

        employee_change_requested.send(sender=__class__, change_request=change_request)

        return change_request
