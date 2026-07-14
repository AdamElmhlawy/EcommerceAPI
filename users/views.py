from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer

class RegisterAPIView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, username=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)

            return Response({"refresh": str(refresh), "access": str(refresh.access_token)})
        
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutAPIVIEW(APIView):

    def post(self, request):

        try:
            refresh_token = request.data['refresh']

            token = RefreshToken(refresh_token)
            token.blacklist()
            
            return Response({"message": "Logged out successfully"})
        except Exception:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)