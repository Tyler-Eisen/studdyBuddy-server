from rest_framework import serializers
from studybuddyapi.models import ConversationContext

class ConversationContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationContext
        fields = ['session_id', 'context_data', 'user_id']  # Adjust the fields based on your model fields
