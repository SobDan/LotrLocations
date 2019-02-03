# from django.db import models


# class Songs(models.Model):
#     # song title
#     title = models.CharField(max_length=255, null=False)
#     # name of artist or group/band
#     artist = models.CharField(max_length=255, null=False)

    # def __str__(self):
    #     return "{} - {}".format(self.title, self.artist)

from django.db import models

 # Create Movie Model
class Location(models.Model):
    region = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    lon = models.DecimalField(max_digits=10, decimal_places=5)
    lat = models.DecimalField(max_digits=10, decimal_places=5)
    



