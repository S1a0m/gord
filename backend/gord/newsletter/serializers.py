from rest_framework import serializers
from .models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['email']


class UnsubscribeSerializer(serializers.Serializer):
    token = serializers.UUIDField()
