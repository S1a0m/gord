from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfessionalExperienceViewSet, TestimonyViewSet

router = DefaultRouter()
router.register(r'experiences', ProfessionalExperienceViewSet, basename='pro-exp')
router.register(r'testimonials', TestimonyViewSet, basename='testimony')

urlpatterns = [
    path('', include(router.urls)),
]
