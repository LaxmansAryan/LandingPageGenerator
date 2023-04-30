from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from uuid import uuid4
from django.conf import settings
from django.urls import reverse
import os

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.user.email, self.uniqueId)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
     
        self.slug = slugify('{} {}'.format(self.section1Title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Profile, self).save(*args, **kwargs)




class Website(models.Model):
    # Standard variable
    section1Title = models.CharField(null=True, blank=True, max_length=200)
    section1Description = models.TextField(null=True, blank=True)
    callToAction = models.CharField(null=True, blank=True, max_length=100)
    section1Image = models.ImageField(default='default.jpg', upload_to='landing_page_images')

    section3Title = models.CharField(null=True, blank=True, max_length=200)
    section3Description = models.TextField(null=True, blank=True)
    section3Image = models.ImageField(default='default.jpg', upload_to='landing_page_images')

    # RELATED FIELDS
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.section1Title, self.uniqueId)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
     
        self.slug = slugify('{} {}'.format(self.section1Title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Website, self).save(*args, **kwargs)

class WebsiteService(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    icon = models.CharField(null=True, blank=True, max_length=200)
    
     # RELATED FIELDS
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
     
        self.slug = slugify('{} {}'.format(self.section1Title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(WebsiteService, self).save(*args, **kwargs)


class WebsiteFeatures(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    icon = models.CharField(null=True, blank=True, max_length=200)
    image = models.ImageField(default='default.jpg', upload_to='landing_page_images')

    # RELATED FIELDS
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
     
        self.slug = slugify('{} {}'.format(self.section1Title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(WebsiteFeatures, self).save(*args, **kwargs)

class Image(models.Model):
    photo = models.ImageField(upload_to="landing_page_images/",null = True,default="")
    date = models.DateTimeField(auto_now_add=True)