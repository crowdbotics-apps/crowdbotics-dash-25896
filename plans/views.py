from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from . import serializers, models


class PlanViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = serializers.PlanSerializer
    queryset = models.Plan.objects.all()