from __future__ import unicode_literals

from django.urls import reverse
from django.db import models

class Startup(models.Model):
      name = models.CharField(max_length=31)
      slug = models.SlugField()
      description = models.TextField()
      founded_date = models.DateField()
      contact = models.EmailField()
      website = models.URLField()

      class Meta:
          ordering = ['name']
          get_latest_by = 'founded_date'

      def __str__(self):
                return self.name


class Tag(models.Model):
    name = models.CharField(
              max_length=31, unique=True)
    slug = models.SlugField(
              max_length=31,
              unique=True,
              help_text='A label for URL config.')

    def get_absolute_url(self):
        return reverse('tag_detail',
                   kwargs={'slug': self.slug})

    class Meta:
          ordering = ['name']

    def __str__(self):
              return self.name


class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField()
    text = models.TextField()
    pub_date = models.DateField()
    startups = models.ManyToManyField(Startup)
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse('post_detail',
                       kwargs={'slug': self.slug})

    def __str__(self):
        return "{} on {}".format(
            self.title,
            self.pub_date.strftime('%Y-%m-%d'))
