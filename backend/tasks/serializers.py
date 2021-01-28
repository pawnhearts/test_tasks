from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer, NestedUpdateMixin
from .models import Task, Hint


class HintSerializer(NestedUpdateMixin, serializers.ModelSerializer):
    class Meta:
        model = Hint
        fields = ['id', 'task', 'hint']


class TaskSerializer(WritableNestedModelSerializer):
    hints = HintSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = ['title', 'description', 'user', 'created', 'due', 'hints']
        read_only_fields = ['user']
