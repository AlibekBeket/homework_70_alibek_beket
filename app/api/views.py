from django.http import JsonResponse
from django.views import View
from issue_tracker.models import Issue

from api.serializers import IssueSerializer


class IssueDetailView(View):
    def get(self, request, *args, **kwargs):
        objects = Issue.objects.filter(id=self.kwargs['pk'])
        serializer = IssueSerializer(objects, many=True)
        return JsonResponse(serializer.data, safe=False)
