# Generated by Django 4.2.2 on 2023-06-19 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('ponto_turistico', '0004_pontoturistico_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='review',
            field=models.ManyToManyField(to='avaliacoes.avaliacao'),
        ),
    ]
