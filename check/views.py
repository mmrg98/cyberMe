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
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt


class SignUpAPIView(CreateAPIView):
	serializer_class = SignUpSerializer


class CheckCard(View):
	def post(self, request, *args, **kwargs):
		card_number = request.POST
		print("--------request.POST----------", request.POST)
		print("--------request.data----------", request.data)
		response = cardpwn(card_number['card_number'])
		return JsonResponse(response)
	
	def get(self, request, *args, **kwargs):
		response = cardpwn(1234567887654321)
		return JsonResponse(response)





