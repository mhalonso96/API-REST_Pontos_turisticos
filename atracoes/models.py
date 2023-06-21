from django.db import models


class Atracao(models.Model):
    name = models.CharField(max_length= 150)
    description = models.TextField()
    opening_hours = models.TextField()
    minimum_age = models.IntegerField()
    photo = models.ImageField(upload_to='atracoes', null=True, blank= True)

    def __str__(self):
        return self.name