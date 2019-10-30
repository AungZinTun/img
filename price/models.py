from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
from portfolio.models import Category
from ckeditor_uploader.fields import RichTextUploadingField



class Price(models.Model):
    title=models.CharField(max_length=225, blank=True, null=True )
    description=RichTextUploadingField(blank=True, null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % self.title
