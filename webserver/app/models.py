from django.db import models

# Create your models here.

class CCTV(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    cctv_url = models.URLField()
