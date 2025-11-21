from rest_framework.routers import DefaultRouter
from .views import BenefitPlanViewSet, BenefitEnrollmentViewSet

router = DefaultRouter()
router.register(r'plans', BenefitPlanViewSet)
router.register(r'enrollments', BenefitEnrollmentViewSet)

urlpatterns = router.urls
