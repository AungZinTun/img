from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name=models.CharField(max_length=30, blank=True, null=True)
    photo=models.ImageField(upload_to='static/img/', blank=True, null=True)
    slug=models.SlugField(default='', blank=True)
    def save(self):
        self.slug=slugify(self.name)
        super(Category, self).save()
    def __str__(self):
        return '%s' % self.name


class Portfolio(models.Model):
    title=models.CharField(max_length=225, blank=True, null=True )
    description=RichTextUploadingField(blank=True, null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % self.title
