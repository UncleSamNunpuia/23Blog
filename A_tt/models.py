from django.db import models

# Create your models here.


class MyModel(models.Model):
    my_file = models.FileField(upload_to='uploads/')
    my_image = models.ImageField(upload_to='uploads/')
