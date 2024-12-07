from rest_framework import viewsets
from .serializers import FaqSerializer
from .models import Faq


class FaqViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
