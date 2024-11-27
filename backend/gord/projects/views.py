from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-release_date')
    serializer_class = ProjectSerializer
