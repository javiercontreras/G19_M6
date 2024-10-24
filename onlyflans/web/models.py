from django.db import models

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    img_url = models.TextField()
    slug = models.SlugField()
    is_private = models.BooleanField()