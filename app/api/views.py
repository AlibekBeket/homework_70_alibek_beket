from rest_framework.views import APIView
from rest_framework.response import Response
from issue_tracker.models import Issue

from api.serializers import IssueSerializer


class IssueDetailView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Issue.objects.filter(id=self.kwargs['pk'])
        serializer = IssueSerializer(objects, many=True)
        return Response(serializer.data)


class IssueUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        objects = Issue.objects.filter(id=self.kwargs['pk']).first()
        serializer = IssueSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
