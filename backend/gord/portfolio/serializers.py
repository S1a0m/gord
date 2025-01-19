from rest_framework import serializers
from .models import ProfessionalExperience, Testimony


class ProfessionalExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalExperience
        fields = ['about', 'proof_link']


class TestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimony
        fields = ['author_name', 'message', 'avatar']
