from rest_framework import serializers

from .models import Hint, Task


class HintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hint
        fields = ["id", "task", "hint"]


class TaskSerializer(serializers.ModelSerializer):
    hints = HintSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = ["title", "description", "user", "created", "due", "hints"]
        read_only_fields = ["user"]
