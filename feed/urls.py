from django.urls import path
from feed.views import ProjectListView, delete_project
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from . import views
from user_account.views import profile_view

urlpatterns = [
    path('delete/<int:project_id>/', delete_project, name='delete_project'),
    path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('accounts/', include('allauth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('feed/<int:project_id>/add_comment/', views.add_comment, name='add_comment'),
    path('profile/', profile_view, name='profile'),  
    path('project/', views.add_project, name='add_project'),
    path('projects/join/<int:project_id>/', views.join_project, name='join_project'),
    path('project/<int:project_id>/delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    
]