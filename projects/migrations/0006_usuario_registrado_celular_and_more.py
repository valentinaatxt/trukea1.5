# Generated by Django 4.1.1 on 2022-10-12 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_remove_destinatarios_direccion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario_registrado',
            name='celular',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario_registrado',
            name='documento',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]