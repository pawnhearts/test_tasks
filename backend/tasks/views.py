import django_filters
from django_filters import FilterSet
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (
    SAFE_METHODS,
    BasePermission,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.response import Response

from .filters import TaskFilter
from .models import Hint, Task
from .permissions import IsAdminUserOrReadOnly
from .serializers import HintSerializer, TaskSerializer


class HintViewSet(viewsets.ModelViewSet):
    """ I assume only staff can add/edit hints """

    serializer_class = HintSerializer
    permission_classes = [IsAdminUserOrReadOnly, IsAuthenticated]
    queryset = Hint.objects.all()
    filterset_fields = ['task']



class TaskViewSet(viewsets.ModelViewSet):
    """ I assume only staff can add/edit hints """

    serializer_class = TaskSerializer
    permission_classes = [IsAdminUserOrReadOnly, IsAuthenticated]
    queryset = Task.objects.all()
    filter_class = TaskFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]

    search_fields = ["title"]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
