from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from authentication.serializer import UserSerializer


class CreateUserView(APIView):

    def post(self, request):
        # Passing our data in the seriealizer
        serializer = UserSerializer(data=request.data)

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
