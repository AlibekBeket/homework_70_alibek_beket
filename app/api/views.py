from rest_framework.views import APIView
from rest_framework.response import Response
from issue_tracker.models import Issue, Project

from api.serializers import IssueSerializer, ProjectSerializer


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


class IssueDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        objects = Issue.objects.filter(id=self.kwargs['pk']).first()
        objects.delete()
        return Response(status=204)


class ProjectDetailView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Project.objects.filter(id=self.kwargs['pk']).first()
        serializer = ProjectSerializer(objects)
        return Response(serializer.data)


class ProjectUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        objects = Project.objects.filter(id=self.kwargs['pk']).first()
        serializer = ProjectSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
