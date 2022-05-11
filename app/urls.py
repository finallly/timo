from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static

from app import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

