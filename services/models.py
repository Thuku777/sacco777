from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe
from PIL import Image

class Service_heading(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True,)
    service_statement = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Heading'
        verbose_name_plural = 'Heading'
        ordering = ['date_posted']

    def __str__(self):
        return self.title



class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=False, null=True, unique=True)
    description = RichTextField()
    icon = models.ImageField(upload_to='icons/%Y/%m/%d/', null=True, blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='Service/%Y/%m/%d/', null=True, blank=False)

    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))
        return "" 

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'slug': self.slug})
    
    
class Solution(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default='business-solution', blank=False, null=True, unique=True)
    statement = models.CharField(max_length=400)
    description = RichTextField()
    count_1 = models.IntegerField(null=True, blank=False)
    fact_1 = models.CharField(max_length=200, null=True, blank=False) 
    count_2 = models.IntegerField(null=True, blank=False)
    fact_2 = models.CharField(max_length=200, null=True, blank=False) 
    count_3 = models.CharField(max_length=200, null=True, blank=False) 
    fact_3 = models.CharField(max_length=200, null=True, blank=False) 
    count_4 = models.CharField(max_length=200, null=True, blank=False) 
    fact_4 = models.CharField(max_length=200, null=True, blank=False) 
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='Solutions/%Y/%m/%d/', null=True, blank=False)
    
    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))
        return ""

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('solution-detail', kwargs={'slug': self.slug})