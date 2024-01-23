from django.db import models

class ConversationContext(models.Model):
    session_id = models.CharField(max_length=100, unique=True)  # Serving unique session realness!
    context_data = models.TextField()  # This is where we spill the tea, storing all that juicy context.

    def __str__(self):
        return f"Session {self.session_id} - Context"
