from .serializers import SignUpSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.contrib.auth.models import User


class SignUpAPIView(CreateAPIView):
	serializer_class = SignUpSerializer
