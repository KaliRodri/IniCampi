from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('edit_avatar/', views.edit_avatar, name='edit_avatar'),
    path('edit_background/', views.edit_background, name='edit_background'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('unsubscribe/<int:project_id>/', views.unsubscribe_from_project, name='unsubscribe_from_project'),
    path('edit_summary/', views.edit_summary, name='edit_summary'),
    path('edit_hard-skills/', views.edit_hard_skills, name='edit_hard_skills'),
]
 