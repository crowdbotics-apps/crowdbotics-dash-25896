from subscriptions.models import Subscription
from rest_framework import serializers
from .models import App
from subscriptions.serializers import SubscriptionSerializer


class AppSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    subscription = SubscriptionSerializer(read_only=True)
    class Meta:
        model = App
        fields = '__all__'
        read_only_fields = ["id", "screenshot", "subscription", "created_at", "updated_at"]
