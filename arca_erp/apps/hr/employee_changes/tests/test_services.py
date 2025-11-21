from django.test import TestCase
from django.contrib.auth.models import User
from apps.hr.people_ops.models import Employee
from ..models import EmployeeChangeRequest, ApprovalRule
from ..services.change_request_service import ChangeRequestService
from ..services.approval_service import ApprovalService
from ..services.apply_change_service import ApplyChangeService
from django.core.exceptions import ValidationError

class EDCServiceTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.approver = User.objects.create(username='approver', is_staff=True)
        self.employee = Employee.objects.create(employee_id='123', first_name='John', last_name='Doe', personal_email='john.doe@example.com')
        ApprovalRule.objects.create(change_type='personal_info', levels=1)
        ChangeRequestService.ALLOWED_CHANGE_TYPES['personal_info'] = ['first_name', 'last_name', 'personal_email']

    def test_create_change_request(self):
        service = ChangeRequestService()
        payload = {'first_name': 'Jane', 'last_name': 'Doe', 'personal_email': 'jane.doe@example.com'}
        change_request = service.create_change_request(
            employee=self.employee,
            requested_by=self.user,
            change_type='personal_info',
            payload_after=payload
        )
        self.assertEqual(change_request.employee, self.employee)
        self.assertEqual(change_request.payload_after['first_name'], 'Jane')
        self.assertIn('first_name', change_request.payload_before)
        self.assertEqual(change_request.payload_before['first_name'], 'John')

    def test_create_change_request_invalid_type(self):
        service = ChangeRequestService()
        with self.assertRaises(ValidationError):
            service.create_change_request(
                employee=self.employee,
                requested_by=self.user,
                change_type='invalid_type',
                payload_after={'field': 'value'}
            )

    def test_approval_workflow(self):
        payload = {'first_name': 'Jane', 'last_name': 'Doe', 'personal_email': 'jane.doe@example.com'}
        change_request = ChangeRequestService.create_change_request(
            employee=self.employee,
            requested_by=self.user,
            change_type='personal_info',
            payload_after=payload
        )

        # Test approval
        ApprovalService.approve_change_request(change_request, self.approver, level=1)
        change_request.refresh_from_db()
        self.assertEqual(change_request.status, 'Approved')

        # Test applying the change
        ApplyChangeService.apply_change(change_request)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.first_name, 'Jane')
        self.assertEqual(change_request.status, 'Applied')

    def test_rejection_workflow(self):
        payload = {'first_name': 'Jane', 'last_name': 'Doe', 'personal_email': 'jane.doe@example.com'}
        change_request = ChangeRequestService.create_change_request(
            employee=self.employee,
            requested_by=self.user,
            change_type='personal_info',
            payload_after=payload
        )
        ApprovalService.reject_change_request(change_request, self.approver, level=1, reason='Typo')
        change_request.refresh_from_db()
        self.assertEqual(change_request.status, 'Rejected')
