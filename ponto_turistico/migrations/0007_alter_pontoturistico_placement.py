# Generated by Django 4.2.2 on 2023-06-20 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localizacoes', '0001_initial'),
        ('ponto_turistico', '0006_pontoturistico_placement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='placement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='localizacoes.localizacao'),
        ),
    ]
