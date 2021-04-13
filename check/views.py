from .serializers import SignUpSerializer
from django.views import View
from rest_framework.generics import CreateAPIView
from django.http import JsonResponse
from django.contrib.auth.models import User
from check.scripts.card.cardpwn import cardpwn



class SignUpAPIView(CreateAPIView):
	serializer_class = SignUpSerializer


class CheckCard(View):

	def get(self, request,card, *args, **kwargs):
		response = cardpwn(card)
		return JsonResponse(response)
