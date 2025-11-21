from rest_framework.routers import DefaultRouter
from .views import EmployeeChangeRequestViewSet

router = DefaultRouter()
router.register(r'employee-changes', EmployeeChangeRequestViewSet)

urlpatterns = router.urls
