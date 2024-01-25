from rest_framework import serializers
from studybuddyapi.models import Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title', 'content', 'category', 'user_id']
