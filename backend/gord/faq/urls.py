from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FaqViewSet

router = DefaultRouter()
router.register('faq', FaqViewSet, basename='faq')

urlpatterns = [
    path('', include(router.urls)),
]
