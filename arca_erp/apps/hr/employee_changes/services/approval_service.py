from ..models import EmployeeChangeRequest, EmployeeApproval, ApprovalRule
from ..signals import employee_change_approved
from django.core.exceptions import PermissionDenied

class ApprovalService:
    @staticmethod
    def approve_change_request(change_request, approver, level, comment=""):
        """
        Approves a change request at a specific level.
        """
        # A real implementation would have more robust permission checks
        approval, created = EmployeeApproval.objects.get_or_create(
            change_request=change_request,
            level=level,
            defaults={'approver': approver, 'status': 'Approved', 'comment': comment}
        )

        if not created and approval.status == 'Approved':
            return approval # Already approved

        if approval.status == 'Rejected':
            raise PermissionDenied("This level has already rejected the request.")

        approval.status = 'Approved'
        approval.approver = approver
        approval.comment = comment
        approval.save()

        # Check if all levels have approved
        rule = ApprovalRule.objects.get(change_type=change_request.change_type)
        if change_request.approvals.filter(status='Approved').count() == rule.levels:
            change_request.status = 'Approved'
            change_request.save()
            employee_change_approved.send(sender=__class__, change_request=change_request)

        return approval

    @staticmethod
    def reject_change_request(change_request, approver, level, reason):
        """
        Rejects a change request at a specific level.
        """
        approval, _ = EmployeeApproval.objects.get_or_create(
            change_request=change_request,
            level=level,
            defaults={'approver': approver, 'status': 'Rejected', 'comment': reason}
        )
        approval.status = 'Rejected'
        approval.comment = reason
        approval.save()

        change_request.status = 'Rejected'
        change_request.rejection_reason = reason
        change_request.save()
        return approval
