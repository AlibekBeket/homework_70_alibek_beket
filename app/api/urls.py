from django.urls import path

from api.views import IssueDetailView, IssueUpdateView, IssueDeleteView

urlpatterns = [
    path('detail/<int:pk>/', IssueDetailView.as_view(), name='api_issue_detail'),
    path('update/<int:pk>/', IssueUpdateView.as_view(), name='api_issue_update'),
    path('delete/<int:pk>/', IssueDeleteView.as_view(), name='api_issue_delete'),
]
