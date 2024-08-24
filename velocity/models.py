from django.db import models

# Create your models here.
class Velocity(models.Model):
    title=models.CharField(max_length=255)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    mobile=models.CharField(max_length=20)
    description=models.CharField(max_length=255)
    
    

