from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from apps.hr.people_core.models import Employee
from ..models import ApprovalRule
from ..services.change_request_service import ChangeRequestService
from datetime import date

class EDCAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password', email='testuser@example.com')
        self.employee = Employee.objects.create(first_name='John', last_name='Doe', email_official='testuser@example.com', email_personal='john.doe@example.com', date_joined=date(2021, 1, 15))
        ApprovalRule.objects.create(change_type='personal_info', levels=1)
        ChangeRequestService.ALLOWED_CHANGE_TYPES['personal_info'] = ['first_name', 'last_name', 'email_personal']


    def test_create_change_request_api(self):
        self.client.force_authenticate(user=self.user)
        url = '/api/data_change/employee-changes/'
        data = {
            'employee': self.employee.employee_id,
            'change_type': 'personal_info',
            'payload_after': {'first_name': 'Jane', 'last_name': 'Doe', 'email_personal': 'jane.doe@example.com'}
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['payload_after']['first_name'], 'Jane')
