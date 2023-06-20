from django.db import models

class Localizacao (models.Model):
    line1= models.CharField(max_length= 255)
    line2= models.CharField(max_length= 255, null= True, blank= True)
    city  = models.CharField(max_length= 100)
    state = models.CharField(max_length= 100)
    country = models.CharField(max_length= 100)
    latitude = models.IntegerField(null= True, blank= True)
    longitude = models.IntegerField(null= True, blank= True)

    def __str__(self) -> str:
        return self. line1
