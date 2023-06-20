from django.db import models
from django.contrib.auth.models import User

class Avaliacao (models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    comment = models.TextField(null= True, blank= True)
    note = models.DecimalField(decimal_places=2, max_digits=3)
    date = models.DateTimeField(auto_now_add= True)

    def __str__(self) -> str:
        return self.user.username