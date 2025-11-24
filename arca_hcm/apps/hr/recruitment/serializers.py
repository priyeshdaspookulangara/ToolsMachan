from rest_framework import serializers
from .models import (
    Requisition, JobPosting, Candidate, Application, Interview,
    Assessment, Offer, BackgroundCheck, HireRecord
)

class RequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisition
        fields = '__all__'

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

class BackgroundCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackgroundCheck
        fields = '__all__'

class HireRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HireRecord
        fields = '__all__'
