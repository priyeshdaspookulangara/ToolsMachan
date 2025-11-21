from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from apps.hr.people_ops.models import Employee
from ..models import ApprovalRule
from ..services.change_request_service import ChangeRequestService

class EDCAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password', email='testuser@example.com')
        self.employee = Employee.objects.create(employee_id='123', first_name='John', last_name='Doe', work_email='testuser@example.com', personal_email='john.doe@example.com')
        ApprovalRule.objects.create(change_type='personal_info', levels=1)
        ChangeRequestService.ALLOWED_CHANGE_TYPES['personal_info'] = ['first_name', 'last_name', 'personal_email']


    def test_create_change_request_api(self):
        self.client.force_authenticate(user=self.user)
        url = '/api/employee_changes/employee-changes/'
        data = {
            'employee': self.employee.id,
            'change_type': 'personal_info',
            'payload_after': {'first_name': 'Jane', 'last_name': 'Doe', 'personal_email': 'jane.doe@example.com'}
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['payload_after']['first_name'], 'Jane')
