from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from feed.views import ProjectListView  # Importa a view do feed
from django.conf import settings
from django.conf.urls.static import static
from user_account.views import profile_view  # Certifique-se de que a view está importada corretamente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feed/', include('feed.urls')),
    path('accounts/', include('allauth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', ProjectListView.as_view(), name='home'),
    path('profile/', profile_view, name='profile'),  # Ação para a função view
    path('profile/', include('user_account.urls')), 
    path('chat/', include('chat.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
