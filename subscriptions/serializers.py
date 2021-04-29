from home.api.v1.serializers import UserSerializer
import plans
from rest_framework import serializers

from .models import Subscription
from plans.serializers import PlanSerializer
from apps.serializers import AppSerializer

class SubscriptionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    plan = PlanSerializer(read_only=True)
    app = AppSerializer(read_only=True)
    class Meta:
        model = Subscription
        fields = '__all__'
        read_only_fields = ["id", "user", "created_at", "updated_at"]
