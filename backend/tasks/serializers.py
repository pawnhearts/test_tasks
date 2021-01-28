from rest_framework import serializers

from .models import Hint, Task


class HintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hint
        fields = ["id", "task", "hint"]


class TaskSerializer(serializers.ModelSerializer):
    hint_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = Task
        fields = ["title", "description", "user", "created", "hint_set"]

