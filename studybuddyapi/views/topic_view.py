from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from studybuddyapi.models import Topic
from studybuddyapi.serializers import TopicSerializer

class TopicView(ViewSet):
    def retrieve(self, request, pk=None):
        try:
            # Retrieve the Topic instance
            topic = Topic.objects.get(pk=pk)

            # Serialize the Topic instance
            serializer = TopicSerializer(topic, context={'request': request})
            data = serializer.data

            return Response(data)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
    def list(self, request):
    # Get all Topic instances
        topics = Topic.objects.all()

        # Filter topics by category if provided in query params
        category = request.query_params.get('category', None)
        if category is not None:
            topics = topics.filter(category=category)

        # Serialize the Topic instances
        serializer = TopicSerializer(topics, many=True)

        return Response(serializer.data)
    def create(self, request):
    
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        topic = Topic.objects.get(pk=pk)

        # Fields from your ERD for Topic
        id = request.data.get("id", topic.id)
        title = request.data.get("title", topic.title)
        content = request.data.get("content", topic.content)
        category = request.data.get("category", topic.category)

        # Set updated values to the topic instance
        topic.id = id
        topic.title = title
        topic.content = content
        topic.category = category

        # Save the updated topic instance
        topic.save()

        return Response({'message': 'Topic Updated'}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
   
        topic = Topic.objects.get(pk=pk)
        topic.delete()
        return Response({'message': 'Topic Destroyed'}, status=status.HTTP_204_NO_CONTENT)
