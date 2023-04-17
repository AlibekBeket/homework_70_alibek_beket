from rest_framework import serializers
from issue_tracker.models import Issue


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('summary', 'description', 'status', 'created_at', 'updated_at', 'type', 'project')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def create(self, validate_data):
        return Issue.objects.create(**validate_data)

    def update(self, instance: Issue, validate_data):
        for field, value in validate_data.items():
            setattr(instance, field, value)
        instance.save()
