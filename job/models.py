from django.db import models

# Create your models here.

class Job(models.Model): #table
    tilte = models.CharField(max_length=100) #colum