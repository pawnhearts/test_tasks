import django_filters
from django_filters import FilterSet
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (SAFE_METHODS, BasePermission,
                                        IsAdminUser, IsAuthenticated)
from rest_framework.response import Response

from .filters import TaskFilter
from .models import Hint, Task
from .permissions import IsAdminUserOrReadOnly
from .serializers import HintSerializer, TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """ I assume only staff can add/edit hints """

    serializer_class = TaskSerializer
    permission_classes = [IsAdminUserOrReadOnly, IsAuthenticated]
    queryset = Task.objects.all()
    filter_class = TaskFilter
    search_fields = ["title"]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(
        detail=True, methods=["post", "put", "patch"], permission_classes=[IsAdminUser]
    )
    def hint(self, request, pk=None):
        """Add or update hint
        Nested relations is pain in drf"""
        task = self.get_object()
        serializer = HintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save().task = task
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["delete"], permission_classes=[IsAdminUser])
    def remove_hint(self, request, pk=None):
        return Response(
            {"deleted": Hint.objects.filter(id=request.data["id"]).delete()}
        )
