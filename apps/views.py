from apps.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from . import serializers, models


class AppViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = serializers.AppSerializer
    queryset = models.App.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        owner_queryset = self.queryset.filter(user=self.request.user)
        return owner_queryset
