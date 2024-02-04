from rest_framework import serializers
from .models import Project, Task, PriorityChoices, StatusChoices

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'  # Include all fields for brevity

class TaskSerializer(serializers.ModelSerializer):
    priority = serializers.ChoiceField(choices=PriorityChoices.choices)
    status = serializers.ChoiceField(choices=StatusChoices.choices)

    class Meta:
        model = Task
        fields = ('id', 'project', 'title', 'description', 'create_date', 'priority', 'status', 'label')

    # # Optional: Customize output for readability
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['priority'] = representation['priority'].label
    #     representation['status'] = representation['status'].label
    #     return representation
