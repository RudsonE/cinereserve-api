from django.urls import path
from .views import ReserveSeatView

urlpatterns = [
    path('<int:session_id>/reserve/', ReserveSeatView.as_view()),
]