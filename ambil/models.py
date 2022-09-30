from django.db import models

class Ambil_Data(models.Model):
    date = models.DateField()
    dono = models.CharField(max_length=255)
    driver = models.CharField(max_length=255)
    nopol = models.CharField(max_length=255)
    qtykgs = models.IntegerField()
    tujuan = models.CharField(max_length=255)
    lokasiambil = models.CharField(max_length=255)
    status = models.CharField(max_length=255)



# class Tujuan(models.Model):
#     tujuan = models.CharField(max_length=255)
#     def __str__(self):
#         return self.tujuan

# class Lokasi_Ambil(models.Model):
#     lokasiambil = models.CharField(max_length=255)
#     def __str__(self):
#         return self.lokasiambil