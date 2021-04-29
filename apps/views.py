from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from . import serializers, models


class AppViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.AppSerializer
    queryset = models.App.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

