from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from authentication.serializer import UserRegisterSerializer, UserLoginSerializer

from django.contrib.auth.models import User


class CreateUserView(APIView):
    def post(self, request):
        # Passing our data in the seriealizer
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  # Throws error if data is empty or not correct
            return Response(
                {
                    "status": True,
                    "message": "User Registered Successfully",
                    "data": None,
                },
                status=status.HTTP_201_CREATED,
            )

        # All serializer error stores in errors
        response = {"status": False, "errors": serializer.errors, "data": None}
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data

            # delete old token
            # uncommnet below line and use it if required.
            # Token.objects.filter(user=user).delete()

            # genrate new token
            token, created = Token.objects.get_or_create(user=user)

            # Success Response
            return Response(
                {
                    "status": True,
                    "message": "Login Successfully",
                    "data": {'token': token.key},
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
