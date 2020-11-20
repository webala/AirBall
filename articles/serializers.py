from rest_framework import serializers
from .models import Article
from django.conf import settings


MAX_TITLE_LENGTH = settings.MAX_TITLE_LENGTH
MAX_NAME_LENGTH = settings.MAX_NAME_LENGTH

class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'publisher'
        ]

    def validate_title(self, value):
        if len(value) > MAX_TITLE_LENGTH:
            raise serializers.ValidationError('The title is too long')
        return value

    def validate_publisher(self, value):
        if len(value) > MAX_TITLE_LENGTH:
            raise serializers.ValidationError('The publisher name is too long')
        return value