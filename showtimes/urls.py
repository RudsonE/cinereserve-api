from django.urls import path
from .views import SessionListView
from .views import SeatMapView

urlpatterns = [
    path('', SessionListView.as_view()),
    path('<int:session_id>/seats/', SeatMapView.as_view())
]