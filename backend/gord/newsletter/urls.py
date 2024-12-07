from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubscriberViewSet

router = DefaultRouter()
router.register('subscribe', SubscriberViewSet, basename='subscribe')

urlpatterns = [
    path('', include(router.urls)),
]
