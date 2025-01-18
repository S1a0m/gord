from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('mahou-tche-gnon/', admin.site.urls),
    path('api/blog/', include('blog.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/newsletter/', include('newsletter.urls')),
    path('api/faq/', include('faq.urls')),
]
