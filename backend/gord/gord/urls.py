from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blog/', include('blog.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/comments/', include('comments.urls')),
    path('api/newsletter/', include('newsletter.urls')),
]
