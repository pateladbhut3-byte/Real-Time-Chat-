from django.db import models
class About(models.Model):
    name=models.CharField(max_length=100)
    about_info=models.CharField(max_length=300)
    discription=models.TextField(max_length=500)

# Create your models here.
