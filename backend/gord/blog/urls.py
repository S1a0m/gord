from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, BlogPostSearchView

router = DefaultRouter()
router.register('blog-posts', BlogPostViewSet, basename='blog-posts')

urlpatterns = [
    path('', include(router.urls)),
    path('blog-search/', BlogPostSearchView.as_view(), name='blog-search'),
]
