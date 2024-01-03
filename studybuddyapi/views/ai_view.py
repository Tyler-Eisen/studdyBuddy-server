from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action  # Import the action decorator
from studybuddyapi.openai_utils import generate_question, review_answer
from studybuddyapi.models import Topic

class OpenAIView(ViewSet):
    
    # Add the @action decorator to create a custom route
    @action(detail=True, methods=['get'], url_path='generate')
    def generate(self, request, pk=None):
        try:
            # Retrieve the Topic instance using the provided primary key (pk)
            topic = Topic.objects.get(pk=pk)
            # Generate a question based on the topic's title
            question = generate_question(topic.title)

            # Return the generated question
            return Response({'question': question}, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def review(self, request, pk=None):
        try:
            # Assuming you're sending the answer and topic ID
            answer = request.data.get('answer')
            # Review the answer using OpenAI's API
            feedback = review_answer(answer)

            # Return the AI feedback
            return Response({'feedback': feedback}, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)

    # Additional methods as needed...
