from django.urls import path
from django.contrib.auth import views as auth_views
from feed.views import ProjectListView
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('', ProjectListView.as_view(), name='home'),
    path('feed/', include('feed.urls')),

]
 