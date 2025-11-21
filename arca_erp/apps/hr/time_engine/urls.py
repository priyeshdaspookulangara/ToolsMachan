from rest_framework.routers import DefaultRouter
from .views import ShiftViewSet, AttendanceViewSet, OvertimeViewSet, LeaveTypeViewSet, LeaveBalanceViewSet

router = DefaultRouter()
router.register(r'shifts', ShiftViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'overtime', OvertimeViewSet)
router.register(r'leave-types', LeaveTypeViewSet)
router.register(r'leave-balances', LeaveBalanceViewSet)

urlpatterns = router.urls
