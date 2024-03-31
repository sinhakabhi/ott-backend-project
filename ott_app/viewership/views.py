# ott_app/viewership/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Viewership
from .serializers import CustomerSerializer, ViewershipSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate


class RegisterView(APIView):
    """
    Customer Register API view
    """

    def post(self, request):
        """
        "POST" REST API Call

        Args:
            request (JOSN): JSON Object

        Returns:
            JSON: An HTTP Response
        """
        try:
            serializer = CustomerSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(f"Error: {str(ex)}", status=status.HTTP_400_BAD_REQUEST)


class HomeView(APIView):
    """
    Home API View
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        "GET" REST API Call

        Args:
            request (JSON): JSON Object

        Returns:
            JSON: An HTTP Response
        """
        try:
            customer = request.user
            viewed_videos = Viewership.objects.filter(customer=customer).order_by(
                "-timestamp"
            )[:10]
            serializer = ViewershipSerializer(viewed_videos, many=True)
            return Response(serializer.data)
        except Exception as ex:
            return Response(f"Error: {str(ex)}", status=status.HTTP_400_BAD_REQUEST)


class WatchVideoView(APIView):
    """
    Watch Video API View
    """
    
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        "POST" REST API Call

        Args:
            request (JSON): JSON Object

        Returns:
            JSON: An HTTP Response
        """
        try:
            serializer = ViewershipSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(customer=request.user)
                return Response(data=f'Added {request.data['video_title']} to your history',status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(f"Error: {str(ex)}", status=status.HTTP_400_BAD_REQUEST)
