from rest_framework.generics import ListAPIView
from .models import Session
from .serializers import SessionSerializer

class SessionListView(ListAPIView):
    serializer_class = SessionSerializer

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Session.objects.filter(movie_id=movie_id)