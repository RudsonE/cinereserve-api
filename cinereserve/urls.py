from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="CineReserve API",
        default_version='v1',
        description="API for movie reservation system",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('movies/', include('movies.urls')),
    path('movies/<int:movie_id>/sessions/', include('showtimes.urls')),
    path('movies/<int:movie_id>/sessions/', include('reservations.urls')),
    path('movies/<int:movie_id>/sessions/', include('reservations.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0))
]