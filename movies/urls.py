from django.urls import path
from .views import MovieListView, MovieDetailView

urlpatterns = [
    path('', MovieListView.as_view()), #lista todos
    path('<int:pk>/', MovieDetailView.as_view()) #busca por id
]