from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Subscriber
from .serializers import SubscriberSerializer, UnsubscribeSerializer


class SubscriberViewSet(viewsets.ViewSet):
    """
    ViewSet pour gérer les abonnements à la newsletter.
    """

    # def list(self, request):
    # """
    # Liste tous les abonnés actifs.
    # """
    # subscribers = Subscriber.objects.filter(is_active=True)
    # serializer = SubscriberSerializer(subscribers, many=True)
    # return Response(serializer.data)

    def create(self, request):
        """
        Permet à un utilisateur de s'abonner.
        """
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            subscriber, created = Subscriber.objects.get_or_create(email=email)
            if not created and subscriber.is_active:
                return Response({"message": "Already subscribed"}, status=status.HTTP_200_OK)
            subscriber.is_active = True
            subscriber.save()
            return Response({"message": "Subscription successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='unsubscribe')
    def unsubscribe(self, request):
        """
        Désabonne un utilisateur via un token.
        """
        serializer = UnsubscribeSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            subscriber = get_object_or_404(Subscriber, unsubscribe_token=token)
            subscriber.is_active = False
            subscriber.save()
            return Response({"message": "You have been unsubscribed"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
