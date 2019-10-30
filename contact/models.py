from django.db import models

# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField

class Contact(models.Model):
    description=RichTextUploadingField(blank=True, null=True)