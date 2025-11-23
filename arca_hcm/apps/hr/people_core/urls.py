from rest_framework.routers import DefaultRouter
from .views import (
    EmployeeViewSet, EmploymentViewSet, OrganizationalUnitViewSet, PositionViewSet,
    AssignmentHistoryViewSet, CompensationStructureMetaViewSet
)

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'employment', EmploymentViewSet)
router.register(r'org/units', OrganizationalUnitViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'assignments', AssignmentHistoryViewSet)
router.register(r'compensation-structures', CompensationStructureMetaViewSet)

urlpatterns = router.urls
