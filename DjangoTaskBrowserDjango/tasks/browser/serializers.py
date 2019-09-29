from rest_framework import serializers
from browser.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task_id', 'name', 'Start_Timestamp', 'End_Timestamp', 'status', 'parent', 'duration']