# Generated by Django 4.1.1 on 2022-11-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_usuario_registrado_dinero'),
    ]

    operations = [
        migrations.AddField(
            model_name='monedas',
            name='habilitar',
            field=models.BooleanField(default=True),
        ),
    ]
