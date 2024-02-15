from django.db import models
from studybuddyapi.models import ConversationContext

class UserResponse(models.Model):
    """
    Model to store user responses.
    """
    context = models.ForeignKey(ConversationContext, on_delete=models.CASCADE)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"UserResponse for Context {self.context_id}"
