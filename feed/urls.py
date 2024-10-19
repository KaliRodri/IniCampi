from django.urls import path
from feed.views import ProjectsListView, TeacherListView, ProjectDetailView, TeacherDetailView

urlpatterns = [
    path('projects/', ProjectsListView.as_view(), name='projects'),
    path('teachers/', TeacherListView.as_view(), name='projects'),
]
