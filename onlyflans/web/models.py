from django.db import models

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    precio = models.IntegerField()
    description = models.TextField()
    img_url = models.TextField()
    slug = models.SlugField()
    is_private = models.BooleanField()

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField()
    customer_email = models.EmailField()
    customer_name = models.TextField()
    message = models.TextField()

