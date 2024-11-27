from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['email', 'name', 'content', 'created_at', 'content_type', 'object_id']
