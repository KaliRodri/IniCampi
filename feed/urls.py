from django.urls import path
from feed.views import ProjectListView, delete_project

urlpatterns = [
    path('', ProjectListView.as_view(), name='home'),
    path('delete/<int:project_id>/', delete_project, name='delete_project'),

]
