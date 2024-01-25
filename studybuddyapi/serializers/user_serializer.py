from rest_framework import serializers
from studybuddyapi.models import User

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for comments"""
    class Meta:
        model = User
        fields = ('id', 
                  'uid', 
                  'name',
               )
        depth = 2
