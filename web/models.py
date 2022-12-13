from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=100)
    dateAdded = models.DateTimeField('added on')
    image = models.ImageField(upload_to='images')
    classification = models.CharField(max_length=50, default='waiting for classification')
    dateClassified = models.DateTimeField('classified on', default=None, null=True, blank=True)

