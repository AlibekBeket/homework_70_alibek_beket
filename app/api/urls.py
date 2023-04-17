from django.urls import path

from api.views import IssueDetailView

urlpatterns = [
    path('detail/<int:pk>/', IssueDetailView.as_view(), name='api_issue_detail'),
]
