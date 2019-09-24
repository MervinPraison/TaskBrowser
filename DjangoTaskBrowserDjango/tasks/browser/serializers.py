from rest_framework import serializers
from browser.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task_id', 'name', 'start_date', 'end_date', 'status', 'parent', 'duration']