from distutils.command.upload import upload
from email.mime import image
from pickle import TRUE
from pyexpat import model
from unicodedata import category
from django.db import models

# Create your models here.
JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)


def image_upload(instance ,filename):
    imagename,extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,instance.id,extension)

class Job(models.Model): #table
    tilte = models.CharField(max_length=100) #colum
    #location
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    description= models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary =models.IntegerField(default=0)
    experiance=models.IntegerField(default=1)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='jobs/')


    def __str__(self):
        return self.tilte




class Category(models.Model):
    name = models.CharField(max_length=25) 
    
    def __str__(self):
        return self.name
