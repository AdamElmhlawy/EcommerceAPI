from django.urls import path
from .views import RegisterAPIView, LoginAPIView, LogoutAPIVIEW

urlpatterns = [
    path('auth/register/', RegisterAPIView.as_view(), name="register"),
    path('auth/login/', LoginAPIView.as_view(), name="login"),
    path('auth/logout/', LogoutAPIVIEW.as_view(), name="logout"),
]
