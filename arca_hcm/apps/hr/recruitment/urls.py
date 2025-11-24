from rest_framework.routers import DefaultRouter
from .views import (
    RequisitionViewSet, JobPostingViewSet, CandidateViewSet, ApplicationViewSet,
    InterviewViewSet, AssessmentViewSet, OfferViewSet, BackgroundCheckViewSet,
    HireRecordViewSet
)

router = DefaultRouter()
router.register(r'requisitions', RequisitionViewSet)
router.register(r'postings', JobPostingViewSet)
router.register(r'candidates', CandidateViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'interviews', InterviewViewSet)
router.register(r'assessments', AssessmentViewSet)
router.register(r'offers', OfferViewSet)
router.register(r'background-checks', BackgroundCheckViewSet)
router.register(r'hire-records', HireRecordViewSet)

urlpatterns = router.urls
