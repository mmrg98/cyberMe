from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class SignUpSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	token = serializers.CharField(allow_blank=True, read_only=True)

	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'token']

	def create(self, validated_data):

		new_user = User(**validated_data)
		new_user.set_password(validated_data['password'])
		new_user.save()
		token = RefreshToken.for_user(new_user)
		validated_data["token"] = str(token.access_token)
		return validated_data
