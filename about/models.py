from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe
from PIL import Image

 
class About(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default='about', blank=False, null=True, unique=True)
    statement = models.CharField(max_length=400)
    description = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='About/%Y/%m/%d/', null=True, blank=False)


    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))
        return "" 

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
        ordering = ['date_posted']

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('about-detail', kwargs={'slug': self.slug})


class Team(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,  blank=False, null=True, unique=True)
    title = models.CharField(max_length=400)
    date_posted = models.DateTimeField(default=timezone.now)
    is_mvp = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='Team/%Y/%m/%d/', null=True, blank=False)

    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))
        return "" 

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Lapset Ajibika Team'
        ordering = ['date_posted']


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('team-detail', kwargs={'slug': self.slug})

