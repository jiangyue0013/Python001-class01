from django.db import models

# Create your models here.
class Comments(models.Model):
    # id django自动创建
    stars = models.IntegerField()
    short = models.CharField(max_length=500)
    sentiment = models.FloatField()
