from rest_framework import viewsets
from .models import BenefitPlan, BenefitEnrollment
from .serializers import BenefitPlanSerializer, BenefitEnrollmentSerializer

class BenefitPlanViewSet(viewsets.ModelViewSet):
    queryset = BenefitPlan.objects.all()
    serializer_class = BenefitPlanSerializer

class BenefitEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = BenefitEnrollment.objects.all()
    serializer_class = BenefitEnrollmentSerializer
