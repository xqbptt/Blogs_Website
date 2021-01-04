from django.db import models

# Create your models here.
class User(models.Model):
    url_field = models.URLField(max_length = 200)
    
