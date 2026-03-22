from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from reservations.models import Reservation
from .models import Session
from .serializers import SessionSerializer

#returns avaiable sessions
class SessionListView(ListAPIView):
    serializer_class = SessionSerializer

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Session.objects.filter(movie_id=movie_id)
    
#returns avaible seats per session
class SeatMapView(APIView):
    def get(self, request, movie_id, session_id):
        seats = []

        for i in range(1, 21):
            reservation = Reservation.objects.filter(
                session_id = session_id,
                seat = i,
                status = "reserved"
            ).first()
            
            if reservation:
                status = "reserved"
            else:
                status = "available"
            
            seats.append({
                "seat": i,
                "status": status
            })

        return Response(seats)