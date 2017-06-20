from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Books(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateField('%m/%d/%Y')
    category=models.CharField(max_length=50)
    in_print=models.BooleanField()
    ## selected option 1, defaulted previously added rows to 'True'
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

