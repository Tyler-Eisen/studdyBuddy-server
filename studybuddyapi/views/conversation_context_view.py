from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from studybuddyapi.models import ConversationContext
from studybuddyapi.serializers import ConversationContextSerializer

class ConversationContextView(ViewSet):
    
    def retrieve(self, request, pk=None):
        try:
            # Retrieve the specific ConversationContext instance
            context = ConversationContext.objects.get(pk=pk)
            serializer = ConversationContextSerializer(context, context={'request': request})
            return Response(serializer.data)
        except ConversationContext.DoesNotExist:
            return Response({'message': 'Context Not Found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return HttpResponseServerError(ex)



    def list(self, request):
        user_id = request.query_params.get('user_id', None)
        if user_id is not None:
            contexts = ConversationContext.objects.filter(user_id=user_id)
        else:
            contexts = ConversationContext.objects.all()

        serializer = ConversationContextSerializer(contexts, many=True, context={'request': request})
        return Response(serializer.data)



    def create(self, request):
        serializer = ConversationContextSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            context = ConversationContext.objects.get(pk=pk)
            serializer = ConversationContextSerializer(context, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Context Updated'}, status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ConversationContext.DoesNotExist:
            return Response({'message': 'Context Not Found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        try:
            context = ConversationContext.objects.get(pk=pk, user_id=request.user)
            context.delete()
            return Response({'message': 'Context Deleted'}, status=status.HTTP_204_NO_CONTENT)
        except ConversationContext.DoesNotExist:
            return Response({'message': 'Context Not Found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return HttpResponseServerError(ex)
