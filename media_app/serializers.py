from rest_framework.serializers import ModelSerializer

from .models import Article, Photo, Video


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
