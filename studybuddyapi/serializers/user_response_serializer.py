from rest_framework import serializers
from studybuddyapi.models import UserResponse

class UserResponseSerializer(serializers.ModelSerializer):
    """
    Serializer for UserResponse model.
    """
    class Meta:
        model = UserResponse
        fields = ['id', 'context', 'answer', 'created_at']
