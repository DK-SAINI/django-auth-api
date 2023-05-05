from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView

# import serializer
from authentication.serializer import UserRegisterSerializer, UserLoginSerializer

from helper.email import send_activation_email


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


class SendActivationEmailView(APIView):
    def post(self, request):
        # Get the email from the request data
        email = request.data.get('email')

        try:
            # Try to get the user with the provided email address
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # If the user doesn't exist, return an error response
            response = {
                'status': False,
                'message': 'Invalid email address',
                'data': None

            }
            return Response(response, status=400)

        if user.is_active:
            # If the user is already active, return an error response
            response = {
                'status': False,
                'message': 'Account already activated',
                'data': None

            }
            return Response(response, status=400)

        # Call the send_activation_email method
        send_activation_email(user)
        response = {
            'status': True,
            'message': 'Activation email sent',
            'data': None

        }
        return Response(response, status=200)

# TODO
class ActivateAccountView(TemplateView):
    template_name = 'activate_account.html'

    def get(self, request, *args, **kwargs):
        try:
            # Try to get the user with the provided auth_token
            user = User.objects.get(auth_token=kwargs['token'])
        except User.DoesNotExist:
            pass
            # If the user doesn't exist, redirect to the activation failed page
            # return redirect(reverse('account_activation_failed'))
        # Set the user as active, clear the auth_token, and save the user model
        user.is_active = True
        user.auth_token = ''
        user.save()
