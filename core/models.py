from django.db import models

# Create your models here.
class Comment(models.Model):
    post_id = models.IntegerField()
    TextField = models.TextField()