from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=50)
    dateAdded = models.DateTimeField('date added')
    image = models.ImageField(upload_to='images')

