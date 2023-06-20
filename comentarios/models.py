from django.db import models
from django.contrib.auth.models import User

class Comentario (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Comentario = models.TextField()
    data = models.DateTimeField(auto_now_add= True)
    approved = models.BooleanField(default= True)

    def __str__(self) -> str:
        return self.user.username

