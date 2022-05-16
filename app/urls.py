from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from media_app.views import ArticleView, PhotoView, VideoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', ArticleView.as_view(
        {'get': 'list'}
    )),
    path('photos/', PhotoView.as_view(
        {'get': 'list'}
    )),
    path('videos/', VideoView.as_view(
        {'get': 'list'}
    ))
]

urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
