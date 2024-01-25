from django.db import models

class Topic(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField() 
    category = models.CharField(max_length=255)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
