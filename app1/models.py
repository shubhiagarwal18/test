from django.db import models

# Create your models here.


class savedata(models.Model):
    name = models.CharField(max_length=50, default="")
    gender = models.CharField(max_length=50)
    issue = models.CharField(max_length=255)
    email = models.EmailField(max_length = 256, default="")
    image = models.ImageField(upload_to='images/', default="")
