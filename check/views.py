from .serializers import SignUpSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.contrib.auth.models import User
from check.scripts.card.cardpwn import cardpwn
from django.views import View
from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


class SignUpAPIView(CreateAPIView):
	serializer_class = SignUpSerializer


class CheckCard(APIView):
	def get(self, request, *args, **kwargs):
		response = cardpwn("jfjfjfj")
		return response





