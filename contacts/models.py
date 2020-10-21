from django.db import models
from django.utils import timezone

class Address(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    statement = models.CharField(max_length=100, blank=False, null=True)
    logo = models.ImageField(upload_to='logo/%Y/%m/%d/', null=True, blank=False)
    address = models.CharField(max_length=50, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    phone = models.CharField(max_length=100, null= True, blank=False)
    instagram = models.CharField(max_length=100, null= True, blank=False)
    facebook = models.CharField(max_length=100, null= True, blank=False)
    twitter = models.CharField(max_length=100, null= True, blank=False)
    youtube = models.CharField(max_length=100, null= True, blank=False)
    worktime = models.CharField(max_length=100, null= True, blank=False, help_text="office time Mon-Fri 09:00-17:00")
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Address'
        

class Contact_heading(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True,)
    contact_statement = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Heading'
        verbose_name_plural = 'Heading'
        ordering = ['date_posted']

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=50, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    phone = models.CharField(max_length=100, null= True, blank=False)
    subject = models.CharField(max_length=100, null= True, blank=False)
    message = models.TextField(null=True, blank=False)
    contact_date = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'slug': self.slug})
