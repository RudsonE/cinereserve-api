from django.urls import path
from .views import ReserveSeatView
from .views import MyTicketsView

urlpatterns = [
    path('<int:session_id>/reserve/', ReserveSeatView.as_view()),
    path('my-tickets/', MyTicketsView.as_view())
]