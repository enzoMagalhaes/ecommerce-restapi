
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterUser(APIView):

	permission_classes = [AllowAny]

	def post(self,request):
		reg_serializer = RegisterUserSerializer(data=request.data)
		if reg_serializer.is_valid():
			newuser= reg_serializer.save()
			if newuser:
				return Response(status=status.HTTP_201_CREATED)
		return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LogoutToken(APIView):
	permission_classes = [IsAuthenticated]

	def post(self,request):
		try:
			refresh_token = request.data['refresh_token']
			token = RefreshToken(refresh_token)
			token.blacklist()
			return Response(status=status.HTTP_204_NO_CONTENT)
		except Exception as e:
			return Response(status=status.HTTP_400_BAD_REQUEST)


class CheckToken(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):

		data = {"auth_status":"OK"}
		return Response(data)