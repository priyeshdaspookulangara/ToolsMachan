from rest_framework.routers import DefaultRouter
from .views import (
    EmployeeSnapshotViewSet, PayComponentViewSet, PayrollScheduleViewSet,
    PayrollRunViewSet, PayrollRunResultViewSet, PayrollInputViewSet,
    RetroAdjustmentViewSet, PayslipViewSet, PayrollJournalEntryViewSet,
    StatutoryRuleViewSet
)

router = DefaultRouter()
router.register(r'snapshots', EmployeeSnapshotViewSet)
router.register(r'pay-components', PayComponentViewSet)
router.register(r'schedules', PayrollScheduleViewSet)
router.register(r'runs', PayrollRunViewSet)
router.register(r'run-results', PayrollRunResultViewSet)
router.register(r'inputs', PayrollInputViewSet)
router.register(r'retro-adjustments', RetroAdjustmentViewSet)
router.register(r'payslips', PayslipViewSet)
router.register(r'journal-entries', PayrollJournalEntryViewSet)
router.register(r'statutory-rules', StatutoryRuleViewSet)

urlpatterns = router.urls
