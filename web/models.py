from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=100)
    dateAdded = models.DateTimeField('date added')
    image = models.ImageField(upload_to='images')
    classification = models.CharField(max_length=50, default='waiting for classification')

