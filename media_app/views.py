from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Article, Photo, Video
from .serializers import (
    ArticleSerializer,
    VideoSerializer,
    PhotoSerializer
)


class ArticleView(ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]
    queryset = Article.objects.all()


class PhotoView(ReadOnlyModelViewSet):
    serializer_class = PhotoSerializer
    permission_classes = [AllowAny]
    queryset = Photo.objects.all()


class VideoView(ReadOnlyModelViewSet):
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]
    queryset = Video.objects.all()
