"""musicAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from membro.api.viewsets import MembroListCreateAPIView, MembroRetrieveUpdateDestroyAPIView
from banda.api.viewsets import BandaListCreateAPIView, BandaRetrieveUpdateDestroyAPIView
from musica.api.viewsets import MusicaListCreateAPIView, MusicaDetailAPIView
from album.api.viewsets import AlbumListCreateAPIView, AlbumRetrieveUpdateDestroyAPIView
from users.api.viewsets import UserCreateAPIView, UserRetrieveUpdateDestroyAPIView, AdminUserCreateAPIView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Music API",
      default_version='v2',
      description="Projeto escolar API",
      terms_of_service="http://escolhaumalicenca.com.br/licencas/mit/#",
      contact=openapi.Contact(email="luisrocha1201@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger',  cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user-create/', UserCreateAPIView.as_view(), name='user-create'),
    path('user-detail/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('adminuser-create', AdminUserCreateAPIView.as_view(), name='adminuser-create'),
    
    path('musica-list-create/', MusicaListCreateAPIView.as_view(), name='musica-list-create'),
    path('musica-detail/<int:pk>/', MusicaDetailAPIView.as_view(), name='musica-detail'),
    path('banda-list-create/', BandaListCreateAPIView.as_view(), name='banda-list-create'),
    path('banda-detail/<int:pk>/', BandaRetrieveUpdateDestroyAPIView.as_view(), name='banda-detail'),
    path('membro-list-create/', MembroListCreateAPIView.as_view(), name='membro-list-create'),
    path('membro-detail/<int:pk>/', MembroRetrieveUpdateDestroyAPIView.as_view(), name='membro-detail'),
    path('album-list-create/', AlbumListCreateAPIView.as_view(), name='album-list-create'),
    path('album-detail/<int:pk>/', AlbumRetrieveUpdateDestroyAPIView.as_view(), name='album-detail'),
]
