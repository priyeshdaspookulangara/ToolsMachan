from rest_framework import viewsets
from .models import (
    Requisition, JobPosting, Candidate, Application, Interview,
    Assessment, Offer, BackgroundCheck, HireRecord
)
from .serializers import (
    RequisitionSerializer, JobPostingSerializer, CandidateSerializer,
    ApplicationSerializer, InterviewSerializer, AssessmentSerializer,
    OfferSerializer, BackgroundCheckSerializer, HireRecordSerializer
)

class RequisitionViewSet(viewsets.ModelViewSet):
    queryset = Requisition.objects.all()
    serializer_class = RequisitionSerializer

class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class BackgroundCheckViewSet(viewsets.ModelViewSet):
    queryset = BackgroundCheck.objects.all()
    serializer_class = BackgroundCheckSerializer

class HireRecordViewSet(viewsets.ModelViewSet):
    queryset = HireRecord.objects.all()
    serializer_class = HireRecordSerializer
