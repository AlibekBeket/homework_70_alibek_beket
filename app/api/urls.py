from django.urls import path

from api.views import IssueDetailView, IssueUpdateView

urlpatterns = [
    path('detail/<int:pk>/', IssueDetailView.as_view(), name='api_issue_detail'),
    path('update/<int:pk>/', IssueUpdateView.as_view(), name='api_issue_update'),
]
