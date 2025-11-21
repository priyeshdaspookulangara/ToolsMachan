from rest_framework import serializers
from .models import BenefitPlan, BenefitEnrollment

class BenefitPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenefitPlan
        fields = '__all__'

class BenefitEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenefitEnrollment
        fields = '__all__'
