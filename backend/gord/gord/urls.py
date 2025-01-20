from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('mahou-tche-gnon/', admin.site.urls),
    path('api/blog/', include('blog.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/newsletter/', include('newsletter.urls')),
    path('api/faq/', include('faq.urls')),
    path('api/portfolio/', include('portfolio.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
