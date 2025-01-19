from rest_framework import viewsets
from .serializers import ProfessionalExperienceSerializer, TestimonySerializer
from .models import ProfessionalExperience, Testimony


class ProfessionalExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProfessionalExperience.objects.all()
    serializer_class = ProfessionalExperienceSerializer


class TestimonyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer
