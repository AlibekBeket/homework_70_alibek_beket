from django.urls import path

from api.views import IssueDetailView, IssueUpdateView, IssueDeleteView, ProjectDetailView, ProjectUpdateView, \
    ProjectDeleteView

urlpatterns = [
    path('issue_detail/<int:pk>/', IssueDetailView.as_view(), name='api_issue_detail'),
    path('issue_update/<int:pk>/', IssueUpdateView.as_view(), name='api_issue_update'),
    path('issue_delete/<int:pk>/', IssueDeleteView.as_view(), name='api_issue_delete'),
    path('project_detail/<int:pk>/', ProjectDetailView.as_view(), name='api_project_detail'),
    path('project_update/<int:pk>/', ProjectUpdateView.as_view(), name='api_project_update'),
    path('project_delete/<int:pk>/', ProjectDeleteView.as_view(), name='api_project_delete'),
]
