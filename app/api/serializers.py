from rest_framework import serializers
from issue_tracker.models import Issue, Project


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'summary', 'description', 'status', 'created_at', 'updated_at', 'type', 'project')
        read_only_fields = ('id', 'created_at', 'updated_at')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 'is_deleted', 'user')
        read_only_fields = ('id', 'is_deleted')
