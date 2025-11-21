from rest_framework.routers import DefaultRouter
from .views import (
    EmployeeViewSet, DepartmentViewSet, PositionViewSet, JobViewSet,
    EmploymentHistoryViewSet, EducationViewSet, DocumentViewSet, BankDetailsViewSet
)

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'employment-history', EmploymentHistoryViewSet)
router.register(r'education', EducationViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'bank-details', BankDetailsViewSet)

urlpatterns = router.urls
