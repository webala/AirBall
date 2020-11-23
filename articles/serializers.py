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

class ArticleSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField(read_only=True)
    content = serializers.SerializerMethodField(read_only=True)
    publisher = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'publisher'
        ]

    def get_title(self, obj):
        return obj.title

    def get_content(self, obj):
        return obj.content

    def get_publisher(self, obj):
        return obj.publisher