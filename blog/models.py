from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
import geocoder
import requests

class Blog(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    owner = models.CharField(max_length=30, blank=True, null=True )
    address = models.TextField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True) 
    property_choice = (
            ('Apartment', 'Apartment'),
            ('Bunglow', 'Bunglow'),
            ('Office', 'Office'),
            ('Shop', 'Shop')
        )
    property_type = models.CharField(max_length=30, blank=True, null=True, choices=property_choice)
    want_choice = (
            ('Lease', 'Lease'),
            ('Rent', 'Rent'),
            ('Sell', 'Sell'),
        )
    want_to = models.CharField(max_length=30, blank=True, null=True, choices=want_choice)
    email_address = models.EmailField(max_length = 254, blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.tomtom(self.address, key='a6rRgUqKXNY9G5djDUGX4GMOWBr3G6BM')
        g = g.latlng  # returns => [lat, long]
        self.latitude = g[0]
        self.longitude = g[1]
        return super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])
