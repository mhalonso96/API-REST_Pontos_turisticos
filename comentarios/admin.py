from django.contrib import admin
from .models import Comentario
from.actions import aprova_comment, reprova_comment

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'approved' ]
    actions = [reprova_comment, aprova_comment]

admin.site.register(Comentario, ComentarioAdmin)