from django.db import models

# Create your models here.
class UserImage(models.Model):
    
     = models.ImageField(upload_to='user_images/')
