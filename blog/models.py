from __future__ import unicode_literals

from django.db import models

class Startup(models.Model):
      name = models.CharField(max_length=31)
      slug = models.SlugField()
      description = models.TextField()
      founded_date = models.DateField()
      contact = models.EmailField()
      website = models.URLField()

class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField()
    text = models.TextField()
    pub_date = models.DateField()
    startups = models.ManyToManyField(Startup)