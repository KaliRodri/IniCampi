from django.urls import path
from . import views

urlpatterns = [
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('edit_avatar/', views.edit_avatar, name='edit_avatar'),
    path('edit_background/', views.edit_background, name='edit_background'),
    path('student-projects/', views.student_projects_view, name='student_projects_view'),
    path('teacher-projects/', views.teacher_projects_view, name='teacher_projects_view'),
    path('unsubscribe/<int:project_id>/', views.unsubscribe_from_project, name='unsubscribe_from_project'),
]
 