from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from .serializers import ReservationSerializer
from django.contrib.auth.models import User
from .models import Reservation

class ReserveSeatView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, movie_id, session_id):
        seat = request.data.get('seat')

        # basic validation
        if not seat:
            return Response(
                {"error": "Seat is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # verify if was reserved
        exists = Reservation.objects.filter(
            session_id=session_id,
            seat=seat,
            status="reserved"
        ).exists()

        if exists:
            return Response(
                {"error": "Seat already reserved"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # create reserve
        Reservation.objects.create(
            user=request.user,
            session_id=session_id,
            seat=seat,
            status="reserved"
        )

        return Response({"message": "Seat reserved"})

class MyTicketsView(ListAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)