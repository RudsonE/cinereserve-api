from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Reservation

class ReserveSeatView(APIView):
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

        # create reserve (temporary without JWT)
        Reservation.objects.create(
            user=User.objects.first(),
            session_id=session_id,
            seat=seat,
            status="reserved"
        )

        return Response({"message": "Seat reserved"})