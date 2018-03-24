from django.db import models

# Create your models here.
class Juejin(models.Model):
    articleUrl = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishtime = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    content = models.TextField()