from django.db import models

class User(models.Model):

    
    name = models.CharField(max_length=255)
    
    uid = models.CharField(max_length=255, unique=True)
    
    id = models.AutoField(primary_key=True)
