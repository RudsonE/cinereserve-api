from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('movies/', include('movies.urls')),
    path('movies/<int:movie_id>/sessions/', include('showtimes.urls')),
    path('movies/<int:movie_id>/sessions/', include('reservations.urls')),
    path('movies/<int:movie_id>/sessions/', include('reservations.urls'))
]