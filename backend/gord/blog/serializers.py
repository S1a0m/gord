from rest_framework import serializers
from .models import BlogPost, Summary


class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ['id', 'summary', 'summary_link']


class BlogPostSerializer(serializers.ModelSerializer):
    summary = SummarySerializer()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'published_date', 'outline', 'link', 'number_read', 'summary']

