from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class LectureDetail(models.Model):
    title = models.CharField(max_length=255, null=False)
    count = models.IntegerField(null=False)

class SearchDetail(models.Model):
    item = models.CharField(max_length=255, null=False)
    title = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    std_date = models.TextField(blank=True, null=True)