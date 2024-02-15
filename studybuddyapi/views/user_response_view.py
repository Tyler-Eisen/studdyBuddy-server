# views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from studybuddyapi.serializers import UserResponseSerializer
from studybuddyapi.models import UserResponse
from studybuddyapi.openai_utils import review_answer

class UserResponseView(APIView):
    """
    View for handling user responses.
    """

    def post(self, request):
        serializer = UserResponseSerializer(data=request.data)
        if serializer.is_valid():
            # Save the user response
            user_response = serializer.save()

            # Call the utility function to review the answer
            reviewed_answer = review_answer(user_response.answer)
            if reviewed_answer is not None:
                # Update the user response with the reviewed answer
                user_response.reviewed_answer = reviewed_answer
                user_response.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Failed to review answer'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
