from rest_framework.views import APIView
from rest_framework.response import Response
from issue_tracker.models import Issue

from api.serializers import IssueSerializer


class IssueDetailView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Issue.objects.filter(id=self.kwargs['pk'])
        serializer = IssueSerializer(objects, many=True)
        return Response(serializer.data)
