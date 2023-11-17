from django.db import models

# Create your models here.

from django.db import models

class MyProject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FileField(upload_to="myproject_images/", blank=True)
