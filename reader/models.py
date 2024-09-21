from django.db import models

# Create your models here.


class Reader(models.Model):

    personal_id = models.CharField(max_length=11, unique=True)
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=20)
    email = models.EmailField(max_length=40, unique=True)

    
    
    