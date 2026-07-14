from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProductSerializer, ProductImageSerializer, CategorySerializer, BrandSerializer

class CategoryCreateAPIVIEW(Viewset)