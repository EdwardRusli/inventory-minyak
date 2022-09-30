from django.db import models

class Tambah_Data(models.Model):
    date = models.DateField()
    pono = models.CharField(max_length=255)
    qtykgs = models.IntegerField()
    vendor = models.CharField(max_length=255)