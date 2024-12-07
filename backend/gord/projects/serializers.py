from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='get_category_display')

    class Meta:
        model = Project
        fields = '__all__'


